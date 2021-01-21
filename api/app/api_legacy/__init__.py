from flask import (
    Flask,
    jsonify,
    abort,
    make_response,
    session,
    request,
    redirect,
    render_template,
    url_for,
    current_app,
    Blueprint
)

# Python standard libraries
import json
import os
import base64
import sys
import datetime

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests
from twilio.rest import Client
from imagekitio import ImageKit

from google.oauth2 import id_token
from google.auth.transport import requests

from ..model import User, Produit, UserType, PlanType, Plan
from .. import client


api_legacy = Blueprint('api_legacy', __name__, url_prefix=(""))
api_v1 = Blueprint('api_v1', __name__, url_prefix=("/api/v1"))

@api_v1.errorhandler(404)
@api_legacy.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@api_v1.errorhandler(400)
@api_legacy.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@api_v1.route("/user")
@api_legacy.route("/user")
def user():
    return jsonify({'nom' : 'alchimiste'})


def get_google_provider_cfg():
    return requests.get(current_app.config['GOOGLE_DISCOVERY_URL']).json()


@api_v1.route("/login")
@api_legacy.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@api_v1.route("/logout")
@api_legacy.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@api_v1.route("/login/callback")
@api_legacy.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(current_app.config['GOOGLE_CLIENT_ID'], current_app.config['GOOGLE_CLIENT_SECRET']),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        user = User(unique_id = userinfo_response.json()["sub"],
                    nom = userinfo_response.json()["given_name"],
                    email = userinfo_response.json()["email"],
                    url_photo = userinfo_response.json()["picture"])
    else:
        return "User email not available or not verified by Google.", 400

    # Doesn't exist? Add it to the database.
    if not User.objects(unique_id=unique_id).first():
        user.save()

    return redirect(url_for("index"))


def start_verification(to, channel='sms'):
    client = Client(current_app.config["TWILIO_ACCOUNT_SID"], current_app.config["TWILIO_AUTH_TOKEN"])

    if channel not in ('sms', 'call'):
        channel = 'sms'

    service = current_app.config['VERIFICATION_SID']

    verification = client.verify \
        .services(service) \
        .verifications \
        .create(to=to, channel=channel, app_hash=current_app.config['APP_HASH'])

    return verification.sid

def check_verification(phone, code):
    client = Client(current_app.config["TWILIO_ACCOUNT_SID"], current_app.config["TWILIO_AUTH_TOKEN"])
    service = current_app.config['VERIFICATION_SID']

    try:
        verification_check = client.verify \
            .services(service) \
            .verification_checks \
            .create(to=phone, code=code)

        if verification_check.status == "approved":
            return True

        else:
            return False

    except Exception as e:
        return False

@api_v1.route('/register_number', methods=['POST'])
@api_legacy.route('/register_number', methods=['POST'])
def register_number():
    current_user.phone_number = request.json['number']
    current_user.save()
    return jsonify({'success': True})

@api_v1.route('/send_verification_code', methods=['POST'])
@api_legacy.route('/send_verification_code', methods=['POST'])
def send_verifacation_code():
    if start_verification(request.json['number']) is None:
        return jsonify({'success' : False})
    current_user.phone_number = request.json['number']
    return jsonify({'success': True})

@api_v1.route('/check_verification_code', methods=['POST'])
@api_legacy.route('/check_verification_code', methods=['POST'])
def check_verifacation_code():
    if check_verification(current_user.phone_number, request.json['code']):
        current_user.save()
        return jsonify({'verify' : True})
    else:
        return jsonify({'verify' : False})

@api_v1.route('/has_phone_number', methods=['GET'])
@api_legacy.route('/has_phone_number', methods=['GET'])
def has_phone_number():
    if not current_user.is_authenticated:
        return jsonify({'has_phone_number' : False})
    if current_user.phone_number is None:
        return jsonify({'has_phone_number' : False})
    else:
        return jsonify({'has_phone_number' : True})

@api_v1.route('/auth_endpoint', methods=['GET'])
@api_legacy.route('/auth_endpoint', methods=['GET'])
def auth_endpoint():
    imagekit = ImageKit(
        private_key=current_app.config['IMAGEKIT_PRIVATE_KEY'],
        public_key=current_app.config['IMAGEKIT_PUBLIC_KEY'],
        url_endpoint =current_app.config['IMAGEKIT_URL_ENDPOINT']
    )
    auth_params = imagekit.get_authentication_parameters()

    return jsonify(auth_params)

@api_v1.route('/verify_oauth2_token/<token>', methods=['GET'])
@api_legacy.route('/verify_oauth2_token/<token>', methods=['GET'])
def verify_oauth2_token(token):
    try:
        userinfo_response = id_token.verify_oauth2_token(token, requests.Request(),current_app.config['GOOGLE_CLIENT_ID'])
        unique_id = userinfo_response["sub"]
        user = User.objects(unique_id=str(unique_id)).first()
        # Doesn't exist? Add it to the database.
        if not user:
            user = User.from_user_info(userinfo_response)

        login_user(user)
        return jsonify({"verify":True})
    except ValueError:
        return jsonify({"verify":False})

@api_v1.route('/users', methods=['GET'])
@api_legacy.route('/users', methods=['GET'])
def all_users():
    return User.objects().to_json()

@api_v1.route('/users/posts_restants', methods=['GET'])
@api_legacy.route('/users/posts_restants', methods=['GET'])
def posts_restants():
    return jsonify({'posts_restants' : current_user.nbr_articles_restant()})

@api_v1.route('/plans')
def plans():
    return jsonify(PlanType.all())

@api_v1.route('/users/<id>', methods=['GET'])
@api_legacy.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.objects(unique_id=str(id)).first()
    if user == None:
        abort(404)
    return user.to_json()

@api_v1.route('/users/<id>/produits', methods=['GET'])
@api_legacy.route('/users/<id>/produits', methods=['GET'])
def get_user_produits(id):
    user = User.objects(unique_id=id).first()
    if user == None:
        abort(404)
    return user.articles_to_json()

@api_v1.route('/users/<id>/plan', methods=['GET'])
@api_legacy.route('/users/<id>/plan', methods=['GET'])
def get_user_plan(id):
    user = User.objects(unique_id=id).first()
    if user == None:
        abort(404)
    return user.plan.to_json()

@api_v1.route('/users/<id>/plan', methods=['POST'])
@api_legacy.route('/users/<id>/plan', methods=['POST'])
def add_plan(id):
    user = User.objects(unique_id=id).first()
    if user == None:
        abort(404)
    user.set_plan(Plan.create(plan_type=PlanType.STANDARD))
    return user.plan.to_json()

def is_product_or_404(request):
    if (not request.json or
        not request.json['prix'] or
        not request.json['categorie'] or
        not request.json['description'] or
        not request.json['url_photo'] or
        not request.json['url_thumbnail_photo'] or
        not request.json['latitude'] or
        not request.json['longitude']):
        abort(400)

@api_v1.route('/users/<id>/produits', methods=['POST'])
@api_legacy.route('/users/<id>/produits', methods=['POST'])
def add_produit(id):
    is_product_or_404(request)
    user = User.objects(unique_id=id).first()
    if user == None:
        abort(404)
    user.add_article_from_dict(request.json)
    return user.articles_to_json()

@api_v1.route('/users/produits', methods=['GET'])
@api_legacy.route('/users/produits', methods=['GET'])
def user_produit():
    user = User.objects(unique_id=current_user.unique_id).first()
    if not user:
        abort(404)
    return user.articles_to_json()

@api_v1.route('/produits', methods=['POST'])
@api_legacy.route('/produits', methods=['POST'])
def add_user_produit():
    is_product_or_404(request)
    user = User.objects(unique_id=current_user.unique_id).first()
    if not user:
        abort(404)
    user.add_article_from_dict(request.json)
    return user.articles_to_json()

@api_v1.route('/produits', methods=['GET'])
@api_legacy.route('/produits', methods=['GET'])
def all_produits():
    return Produit.objects().to_json()

@api_v1.route('/best_match_produits', methods=['GET'])
def best_match_produits():
    longitude = request.args.get('longitude', None)
    latitude = request.args.get('latitude', None)
    items_per_page = int(request.args.get('items_per_page', 10))
    page_nb = int(request.args.get('page_nb', 1))
    if(longitude == None or latitude == None):
        return Produit.order_by_created_desc(page_nb=page_nb, items_per_page=items_per_page).to_json()
    distanceInKm = 100
    return Produit.best_match(loc=[float(longitude), float(latitude)], max_distance=distanceInKm/111, nbr=200).to_json()

@api_v1.route('/produits/<id>', methods=['GET'])
@api_legacy.route('/produits/<id>', methods=['GET'])
def get_produit(id):
    print(id)
    produit = Produit.objects(id=id).first()
    if produit == None:
        abort(404)
    return produit.to_json()

@api_v1.route('/produits/<id>', methods=['DELETE'])
@api_legacy.route('/produits/<id>', methods=['DELETE'])
def delete_produit(id):
    produit = Produit.objects(id=id).first()
    if user == None:
        abort(404)
    produit.delete()
    return jsonify({'resultat' : True})

@api_v1.route('/produits/<id>', methods=['PUT'])
@api_legacy.route('/produits/<id>', methods=['PUT'])
def update_produit(id):
    is_product_or_404()

    produit = Produit.objects(id=id).first()
    if produit == None:
        abort(404)

    produit.prix = request.json['prix'],
    produit.categorie = request.json['categorie'],
    produit.description = request.json['description']
    produit.save()

    return jsonify({'produit': produit.to_json()}), 201

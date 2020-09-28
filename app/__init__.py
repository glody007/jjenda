import os
from flask import Flask, current_app, send_file, session
from flask_login import LoginManager, login_manager
from flask_cors import CORS
from oauthlib.oauth2 import WebApplicationClient

from .api import api_bp
from .client import client_bp
from .api_legacy import api_legacy
from .api_legacy import api_v1
from .model import User

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
app.register_blueprint(api_legacy)
app.register_blueprint(api_v1)
# app.register_blueprint(client_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

client = WebApplicationClient(app.config['GOOGLE_CLIENT_ID'])

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.before_request
@api_v1.before_request
@api_legacy.before_request
def before_request():
    session.permanent = True
    session.modified = True
    current_app.permanent_session_lifetime = current_app.config['REMEMBER_COOKIE_DURATION']

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.objects(unique_id=str(user_id)).first()

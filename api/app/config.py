"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from os.path import dirname, abspath
from app import app
import datetime
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

class Config(object):
    env_path = Path(dirname(dirname(abspath(__file__))) + "/.env")
    if env_path.is_file():
        load_dotenv(dotenv_path=env_path)

    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    # conigure login_user(remember=True) valid for 7days, default=1year
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=365)
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = os.getenv("GOOGLE_DISCOVERY_URL")
    IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
    IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
    IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

app.config.from_object('app.config.Config')

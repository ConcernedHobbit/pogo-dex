from flask import Flask, flash
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pogodex.db"
    app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = None

@login_manager.user_loader
def load_user(user_id):
    return Trainer.query.get(user_id)

from functools import wraps

def login_required(_func=None, *, admin=False):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                flash("Please log in to use this functionality", "info")
                return login_manager.unauthorized()

            if admin and not current_user.admin:
                flash("You need to be an admin to do that.", "info")
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views

from application.pokemon import models
from application.pokemon import views

from application.auth import models
from application.auth import views

from application.auth.models import Trainer
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

try:
    db.create_all()
except:
    pass

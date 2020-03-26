from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pogodex.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application import views

from application.pokemon import models
from application.pokemon import views

from application.auth import models
from application.auth import views

from application.auth.models import Trainer
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return Trainer.query.get(user_id)

db.create_all()

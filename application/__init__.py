# Flask (web framework) import & initialization
from flask import Flask
app = Flask(__name__)

# SQLAlchemy for database usage
from flask_sqlalchemy import SQLAlchemy
# Database to use is "pogodex.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pogodex.db"
# Debugging: print all SQL queries
app.config["SQLALCHEMY_ECHO"] = True
# Create db object for interacting with the database
db = SQLAlchemy(app)

# Import views for routing
from application import views

# Import pokemon model and views for database and routing
from application.pokemon import models
from application.pokemon import views

# Create necessary database tables
db.create_all()

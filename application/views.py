from flask import render_template
from flask_login import current_user
from application import app
from application.pokemon.models import Pokemon, Pogodex
from application.auth.models import Trainer

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("index.html",
                amount_released = Pokemon.amount_released(),
                amount_caught = Pogodex.amount_caught(current_user.id),
                average_caught = Pogodex.average_caught(),
                amount_trainers = Trainer.amount())
    else:
        return render_template("index.html",
                amount_released = Pokemon.amount_released(),
                average_caught = Pogodex.average_caught(),
                amount_trainers = Trainer.amount())

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
import bcrypt

from application import app, db
from application.auth.models import Trainer
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    next_page = request.args.get("next", default = url_for("index"))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm(), next_page = next_page)

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form, next_page = next_page)

    trainer = Trainer.query.filter_by(
            username = form.username.data
            ).first()

    if not trainer:
        flash("No such username or password.", "error")
        return render_template("auth/loginform.html", form = form, next_page = next_page)

    password = form.password.data.encode()
    db_password = trainer.password
    if isinstance(trainer.password, str):
        db_password = trainer.password.encode()

    if not bcrypt.checkpw(password, db_password):
        flash("No such username or password.", "error")
        return render_template("auth/loginform.html", form = form, next_page = next_page)

    login_user(trainer)
    return redirect(next_page)

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(request.args.get("next", default = url_for("index")))

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)
    if not form.validate():
        return render_template("auth/signupform.html", form = form)

    password = form.password.data.encode()
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)
    if isinstance(hash, bytes):
        hash = hash.decode('utf-8')

    trainer = Trainer(form.username.data, hash)

    db.session.add(trainer)
    db.session().commit()

    flash("Trainer created. Please log in.", "info")
    return redirect(url_for("auth_login"))

from application import app, db
from flask import redirect, render_template, request, url_for
from application.pokemon.models import Pokemon

@app.route("/pokemon/new/")
def pokemon_form():
    return render_template("pokemon/new.html")

@app.route("/pokemon/", methods=["GET"])
def pokemon_index():
    return render_template("pokemon/list.html", pokemon_list = Pokemon.query.all())

@app.route("/pokemon/", methods=["POST"])
def pokemon_create():
    print(request.form.get("id"))
    print(request.form.get("name"))
    print(request.form.get("generation"))
    print(request.form.get("released"))
    p = Pokemon(
            request.form.get("id"),
            request.form.get("name"),
            request.form.get("generation"),
            True if (request.form.get("released") == "on") else False
            )

    db.session.add(p)
    db.session().commit()

    return redirect(url_for("pokemon_index"))

@app.route("/pokemon/<pokemon_id>/release/", methods=["POST"])
def pokemon_release(pokemon_id):
    p = Pokemon.query.get(pokemon_id)
    p.released = True
    db.session().commit()

    return redirect(url_for("pokemon_index"))

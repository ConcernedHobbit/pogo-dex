from application import app, db
from flask import redirect, render_template, request, url_for
from application.pokemon.models import Pokemon
from application.pokemon.forms import PokemonForm

@app.route("/pokemon/new/")
def pokemon_form():
    return render_template("pokemon/new.html", form = PokemonForm())

@app.route("/pokemon/", methods=["GET"])
def pokemon_index():
    return render_template("pokemon/list.html", pokemon_list = Pokemon.query.all())

@app.route("/pokemon/", methods=["POST"])
def pokemon_create():
    form = PokemonForm(request.form)

    if not form.validate():
        return render_template("pokemon/new.html", form = form)

    p = Pokemon(
            form.id.data,
            form.name.data,
            form.generation.data,
            form.released.data
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

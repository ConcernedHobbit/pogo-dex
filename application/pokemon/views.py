from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from application.pokemon.models import Pokemon, Pogodex
from application.pokemon.forms import PokemonForm

@app.route("/pokemon/new/")
@login_required(admin=True)
def pokemon_form():
    return render_template("pokemon/new.html", form = PokemonForm())

@app.route("/pokemon/", methods=["GET"])
def pokemon_index():
    return render_template("pokemon/list.html", pokemon_list = Pokemon.query.order_by(Pokemon.id).all())

@app.route("/pokemon/<pokemon_id>/add", methods=["POST", "GET"])
@login_required
def pokemon_add(pokemon_id):
    p = Pokemon.query.get(pokemon_id)
    if not p.released:
        flash("That Pokémon has not been released.", "warning")
        return redirect(url_for("pokemon_index"))

    check = Pogodex.query.filter_by(
            trainer_id = current_user.id,
            pokemon_id = pokemon_id
            ).first()

    if check:
        print(check)
        flash("You already have that Pokémon in your Pokédex.", "warning")
        return redirect(url_for("pokemon_index"))

    dex_entry = Pogodex(current_user.id, pokemon_id)

    db.session.add(dex_entry)
    db.session.commit()

    return redirect(url_for("pokemon_index"))


@app.route("/pokemon/", methods=["POST"])
@login_required(admin=True)
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
    db.session.commit()

    return redirect(url_for("pokemon_index"))

@app.route("/pokemon/<pokemon_id>/release/", methods=["POST", "GET"])
@login_required(admin=True)
def pokemon_release(pokemon_id):
    p = Pokemon.query.get(pokemon_id)
    p.released = True
    db.session.commit()

    return redirect(url_for("pokemon_index"))

@app.route("/pokemon/<pokemon_id>/delete", methods=["POST", "GET"])
@login_required(admin=True)
def pokemon_delete(pokemon_id):
    p = Pokemon.query.get(pokemon_id)
    db.session.delete(p)
    db.session.commit()

    flash(f"Deleted {p.name} from existance.", "info")
    return redirect(url_for("pokemon_index"))

@app.route("/pokemon/<pokemon_id>/edit", methods=["GET", "POST"])
@login_required(admin=True)
def pokemon_edit(pokemon_id):
    p = Pokemon.query.get(pokemon_id)

    if not p:
        flash("No Pokémon with that ID was found.", "warning")
        return redirect(url_for("pokemon_index"))

    if request.method == "GET":
        form = PokemonForm()
        del form.id

        form.name.data = p.name
        form.generation.data = p.generation
        form.released.data = p.released

        return render_template("pokemon/edit.html", pokemon_id = pokemon_id, form = form)

    form = PokemonForm(request.form)
    del form.id

    if not form.validate():
        return render_template("pokemon/edit.html", pokemon_id = pokemon_id, form = form)

    p.name = form.name.data
    p.generation = form.generation.data
    p.released = form.released.data

    db.session.commit()

    return redirect(url_for("pokemon_index"))

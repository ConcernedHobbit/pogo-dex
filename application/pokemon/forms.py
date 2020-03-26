from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, validators
from wtforms.widgets import html5

class PokemonForm(FlaskForm):
    id = IntegerField(
            label = "ID",
            widget = html5.NumberInput(),
            validators = [
                validators.NumberRange(min=1),
                validators.InputRequired()
                ]
            )
    name = StringField(
            label = "Name",
            validators = [
                validators.Length(min=1),
                validators.InputRequired()
                ]
            )
    generation = IntegerField(
            label = "Generation",
            widget = html5.NumberInput(),
            validators = [
                validators.NumberRange(min=1),
                validators.InputRequired()
                ]
            )
    released = BooleanField(
            label = "Released"
            )

    class Meta:
        csrf = False

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField(
            label = "Username",
            validators = [
                validators.InputRequired()
                ]
            )
    password = PasswordField(
            label = "Password",
            validators = [
                validators.InputRequired()
                ]
            )

    class Meta:
        csrf = False

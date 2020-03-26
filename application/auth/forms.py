from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators

class SignupForm(FlaskForm):
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
    submit = SubmitField(label = "Sign up")

    class Meta:
        csrf = False

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
    submit = SubmitField(label = "Log in")

    class Meta:
        csrf = False

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
   company_email = EmailField(label='Company Email: ', validators=[DataRequired()])
   password = PasswordField(label='Password: ', validators=[DataRequired()])
   submit = SubmitField(label='Sign In')
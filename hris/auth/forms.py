from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, InputRequired

class LoginForm(FlaskForm):
   company_email = EmailField(label='Company Email: ', validators=[DataRequired()])
   password = PasswordField(label='Password: ', validators=[DataRequired()])
   submit = SubmitField(label='Sign In')
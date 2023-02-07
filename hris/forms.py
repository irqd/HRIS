from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, InputRequired
from hris.models import Users

class LoginForm(FlaskForm):
   email = EmailField(label='Work Email: ', validators=[DataRequired()])
   password = PasswordField(label='Password: ', validators=[DataRequired()])
   submit = SubmitField(label='Sign In')


#Modals

class DepartmentModal(FlaskForm):
   departmentList = SelectField(label = 'Choose Department:', validators=[InputRequired()])
   #TODO
   confirm = SubmitField(label='Confirm')
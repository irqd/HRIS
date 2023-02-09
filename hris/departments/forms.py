from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, InputRequired
from hris.models import Users

class DepartmentModal(FlaskForm):
   departmentList = SelectField(label = 'Choose Department:', validators=[InputRequired()])
   #TODO
   confirm = SubmitField(label='Confirm')
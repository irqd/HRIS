from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, InputRequired

class DeleteModal(FlaskForm):
   delete = SubmitField(label='Delete')

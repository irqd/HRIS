from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, InputRequired
from hris.models import Users

class DeleteDepartmentModal(FlaskForm):
   delete = SubmitField(label='Delete')


class DeletePositionModal(FlaskForm):
   delete = SubmitField(label='Delete')


class DepartmentForm(FlaskForm):
   department_name = StringField(label='Department Name', validators=[DataRequired()])
   supervisor = StringField(label='Supervisor', validators=[DataRequired()])
   description = TextAreaField(label='Description')

class PositionForm(FlaskForm):
   position_name = StringField(label='Position Name', validators=[DataRequired()])
   position_status = SelectField(label='Status', choices=[('hiring', 'Hiring'), ('full', 'Full')], validators=[DataRequired()])
   description = TextAreaField(label='Description', validators=[DataRequired()])


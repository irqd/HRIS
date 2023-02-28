from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField, SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, ValidationError)

from hris.models import Users


class DeleteDepartmentModal(FlaskForm):
   delete = SubmitField(label='Delete')


class DeletePositionModal(FlaskForm):
   delete = SubmitField(label='Delete')


class DepartmentForm(FlaskForm):
   department_name = StringField(label='Department Name', validators=[DataRequired()])
   manager = StringField(label='Manager')
   description = TextAreaField(label='Description')


class PositionForm(FlaskForm):
   position_name = StringField(label='Position Name', validators=[DataRequired()])
   position_status = SelectField(label='Status', choices=[('hiring', 'Hiring'), ('full', 'Full')], validators=[DataRequired()])
   description = TextAreaField(label='Description', validators=[DataRequired()])


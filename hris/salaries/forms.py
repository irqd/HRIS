from flask_wtf import FlaskForm
import re
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField, IntegerField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp, Optional)

class AddSalaryModal(FlaskForm):
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   amount = IntegerField(label='Amount', render_kw={"placeholder": "e.g. 10000 (for ten thousand dollars)"}, validators=[DataRequired()])
   per_hour = IntegerField(label='Per Hour', render_kw={"placeholder": "e.g. 8 (for 8 hours per amount)"}, validators=[DataRequired()])
   submit = SubmitField(label='Add Salary')

class EditSalaryModal(FlaskForm):
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   amount = IntegerField(label='Amount', render_kw={"placeholder": "e.g. 10000 (for ten thousand dollars)"}, validators=[DataRequired()])
   per_hour = IntegerField(label='Per Hour', render_kw={"placeholder": "e.g. 8 (for 8 hours per amount)"}, validators=[DataRequired()])
   submit = SubmitField(label='Add Salary')

class DeleteSalaryModal(FlaskForm):
   delete = SubmitField(label='Delete Salary')
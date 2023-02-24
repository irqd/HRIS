from flask_wtf import FlaskForm
import re
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField, IntegerField, FloatField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp, Optional)


class AddSalaryModal(FlaskForm):    
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   daily_rate = FloatField(label='Daily Rate', render_kw={"placeholder": "Daily Rate"}, validators=[DataRequired()])
   hourly_rate = FloatField(label='Hourly Rate', render_kw={"placeholder": "Hourly Rate"}, validators=[DataRequired()])
   bir_tax = FloatField(label='BIR', render_kw={"placeholder": "BIR"})
   sss_tax = FloatField(label='SSS', render_kw={"placeholder": "SSS"}, validators=[DataRequired()])
   phil_health_tax = FloatField(label='Phil Health', render_kw={"placeholder": "Phil Health"}, validators=[DataRequired()])
   pag_ibig_tax = FloatField(label='Pag Ibig', render_kw={"placeholder": "Pag Ibig"}, validators=[DataRequired()])
   ot_rate = FloatField(label='OT Rate', render_kw={"placeholder": "OT Rate"}, validators=[DataRequired()])
   allowance = FloatField(label='Allowance', render_kw={"placeholder": "Allowance"}, validators=[DataRequired()])
   submit = SubmitField(label='Add Salary')

class EditSalaryModal(FlaskForm):
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   daily_rate = FloatField(label='Daily Rate', render_kw={"placeholder": "Daily Rate"}, validators=[DataRequired()])
   hourly_rate = FloatField(label='Hourly Rate', render_kw={"placeholder": "Hourly Rate"}, validators=[DataRequired()])
   bir_tax = FloatField(label='BIR', render_kw={"placeholder": "BIR"})
   sss_tax = FloatField(label='SSS', render_kw={"placeholder": "SSS"}, validators=[DataRequired()])
   phil_health_tax = FloatField(label='Phil Health', render_kw={"placeholder": "Phil Health"}, validators=[DataRequired()])
   pag_ibig_tax = FloatField(label='Pag Ibig', render_kw={"placeholder": "Pag Ibig"}, validators=[DataRequired()])
   ot_rate = FloatField(label='OT Rate', render_kw={"placeholder": "OT Rate"}, validators=[DataRequired()])
   allowance = FloatField(label='Allowance', render_kw={"placeholder": "Allowance"}, validators=[DataRequired()])
   submit = SubmitField(label='Edit Salary')

class DeleteSalaryModal(FlaskForm):
   delete = SubmitField(label='Delete Salary')
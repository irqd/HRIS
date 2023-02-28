import re

from flask_wtf import FlaskForm
from wtforms import (DateField, EmailField, FileField, FloatField, FormField,
                     HiddenField, IntegerField, PasswordField, SelectField,
                     StringField, SubmitField, TextAreaField, TimeField,
                     validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, NumberRange, Optional, Regexp,
                                ValidationError)


class ZeroOrGreater(InputRequired):
    def __init__(self, message=None):
        super().__init__(message=message)

    def __call__(self, form, field):
        if not (field.data == 0 or (field.data is not None and field.data > 0)):
            message = self.message
            if message is None:
                message = field.gettext('Value must be zero or greater.')
            raise ValueError(message)

class AddSalaryModal(FlaskForm):    
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   daily_rate = FloatField(label='Daily Rate', render_kw={"placeholder": "Daily Rate"}, validators=[ZeroOrGreater()])
   hourly_rate = FloatField(label='Hourly Rate', render_kw={"placeholder": "Hourly Rate"}, validators=[ZeroOrGreater()])
   bir_tax = FloatField(label='BIR', render_kw={"placeholder": "BIR"}, validators=[ZeroOrGreater()])
   sss_tax = FloatField(label='SSS', render_kw={"placeholder": "SSS"}, validators=[ZeroOrGreater()])
   phil_health_tax = FloatField(label='Phil Health', render_kw={"placeholder": "Phil Health"}, validators=[ZeroOrGreater()])
   pag_ibig_tax = FloatField(label='Pag Ibig', render_kw={"placeholder": "Pag Ibig"}, validators=[ZeroOrGreater()])
   ot_rate = FloatField(label='OT Rate', render_kw={"placeholder": "OT Rate"}, validators=[ZeroOrGreater()])
   allowance = FloatField(label='Allowance', render_kw={"placeholder": "Allowance"}, validators=[ZeroOrGreater()])
   submit = SubmitField(label='Add Salary')

class EditSalaryModal(FlaskForm):
   salary_name = StringField(label='Name', validators=[DataRequired()])
   description = StringField(label='Description', validators=[DataRequired()])
   daily_rate = FloatField(label='Daily Rate', render_kw={"placeholder": "Daily Rate"}, validators=[ZeroOrGreater()])
   hourly_rate = FloatField(label='Hourly Rate', render_kw={"placeholder": "Hourly Rate"}, validators=[ZeroOrGreater()])
   bir_tax = FloatField(label='BIR', render_kw={"placeholder": "BIR"}, validators=[ZeroOrGreater()])
   sss_tax = FloatField(label='SSS', render_kw={"placeholder": "SSS"}, validators=[ZeroOrGreater()])
   phil_health_tax = FloatField(label='Phil Health', render_kw={"placeholder": "Phil Health"}, validators=[ZeroOrGreater()])
   pag_ibig_tax = FloatField(label='Pag Ibig', render_kw={"placeholder": "Pag Ibig"}, validators=[ZeroOrGreater()])
   ot_rate = FloatField(label='OT Rate', render_kw={"placeholder": "OT Rate"}, validators=[ZeroOrGreater()])
   allowance = FloatField(label='Allowance', render_kw={"placeholder": "Allowance"}, validators=[ZeroOrGreater()])
   submit = SubmitField(label='Edit Salary')

class DeleteSalaryModal(FlaskForm):
   delete = SubmitField(label='Delete Salary')
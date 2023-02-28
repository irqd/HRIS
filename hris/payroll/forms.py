import re

from flask_wtf import FlaskForm
from wtforms import (DateField, EmailField, FileField, FloatField, FormField,
                     HiddenField, IntegerField, PasswordField, SelectField,
                     StringField, SubmitField, TextAreaField, TimeField,
                     validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, Optional, Regexp, ValidationError)


class DeclinePayslipForm(FlaskForm):
   decline = SubmitField(label='Decline')


class ApprovePayslipForm(FlaskForm):
   approve = SubmitField(label='Approve')

class CancelPayslipForm(FlaskForm):
   cancel = SubmitField(label='Cancel')

class RefreshPayrollForm(FlaskForm):
   refresh = SubmitField(label='Refresh')

class EditPayslipForm(FlaskForm):
   total_regular_hours = FloatField(label='Total Regular Hours', validators=[DataRequired()])
   pre_ot_hours = FloatField(label='Pre OT Hours', validators=[DataRequired()])
   post_ot_hours = FloatField(label='Post OT Hours', validators=[DataRequired()])
   allowance = FloatField(label='Allowance', validators=[DataRequired()])

   edit = SubmitField(label='Edit')
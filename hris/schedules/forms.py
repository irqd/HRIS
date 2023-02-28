import re
from datetime import datetime, timedelta

from flask_wtf import FlaskForm
from wtforms import (DateField, EmailField, FileField, FormField, HiddenField,
                     PasswordField, SelectField, StringField, SubmitField,
                     TextAreaField, TimeField, validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, Regexp, ValidationError)


class AddScheduleModal(FlaskForm):

   start_date = StringField(label='Start Date', validators=[DataRequired()])
   end_date = StringField(label='End Date', validators=[DataRequired()])
   
   start_shift = StringField(label='Start Shift', validators=[DataRequired()])
   end_shift = StringField(label='End Shift', validators=[DataRequired()])
   

   submit = SubmitField(label='Add Schedule')


class EditScheduleModal(FlaskForm):
   start_shift = StringField(label='Start Shift', validators=[DataRequired()])
   end_shift = StringField(label='End Shift', validators=[DataRequired()])
   schedule_id = StringField(validators=[DataRequired()])

   checked_in = StringField(label='Checked In', validators=[DataRequired()])
   checked_out = StringField(label='Checked Out', validators=[DataRequired()])

   submit = SubmitField(label='Edit')
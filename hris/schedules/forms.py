from flask_wtf import FlaskForm
import re
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp)

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

   submit = SubmitField(label='Edit Schedule')
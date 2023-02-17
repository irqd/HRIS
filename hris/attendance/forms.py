from flask_wtf import FlaskForm
import re
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp)


class CheckInForm(FlaskForm):
   schedule_id = StringField(validators=[DataRequired()])
   check_in = StringField(validators=[DataRequired()])
   submit = SubmitField(label='Check In')


class CheckOutForm(FlaskForm):
   schedule_id = StringField(validators=[DataRequired()])
   check_out = StringField(validators=[DataRequired()])
   submit = SubmitField(label='Check Out')
   

class LeaveRequestForm(FlaskForm):
  
   type = SelectField(label='Leave Type:', choices=[('sick_leave', 'Sick Leave'),\
                                                   ('sil', 'SIL'),\
                                                   ('maternity_leave', 'Maternity Leave'),\
                                                   ('paternity_leave', 'Paternity Leave'),\
                                                   ('vacation_leave', 'Vacation Leave'),\
                                                   ('parental_leave', 'Parental Leave'),\
                                                   ('rehabilitation_leave', 'Rehabilitation Leave'),\
                                                   ('study_leave', 'Study Leave')\
                                                   ], validators=[DataRequired()])
   start_date = StringField(label='Start Date:', validators=[DataRequired()])
   end_date = StringField(label='End Date:',validators=[DataRequired()])
   submit = SubmitField(label='Send Leave Request')
   
from flask_wtf import FlaskForm
import re
from datetime import datetime, timedelta
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp)


class AnnouncementModal(FlaskForm):
   announced_by = StringField(label='Announced By',validators=[DataRequired()])
   title = StringField(label='Title', validators=[DataRequired()])
   message = TextAreaField(label='Message', validators=[DataRequired()])   
   submit = SubmitField(label='Add Announcement')  


class EditAnnouncement(FlaskForm):
   submit = SubmitField(label='Edit Announcement')
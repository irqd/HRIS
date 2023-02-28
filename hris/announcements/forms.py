import re
from datetime import datetime, timedelta

from flask_wtf import FlaskForm
from wtforms import (DateField, EmailField, FileField, FormField, HiddenField,
                     PasswordField, SelectField, StringField, SubmitField,
                     TextAreaField, TimeField, validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, Regexp, ValidationError)


class AnnouncementModal(FlaskForm):
   announced_by = StringField(label='Announced By',validators=[DataRequired()])
   title = StringField(label='Title', validators=[DataRequired()])
   message = TextAreaField(label='Message', validators=[DataRequired()])   
   submit = SubmitField(label='Add Announcement')  


class EditAnnouncement(FlaskForm):
   submit = SubmitField(label='Edit Announcement')
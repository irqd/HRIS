from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, FileField, validators
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp, Optional)

class AccountForm(FlaskForm):
   image_path = FileField(label='Employee Picture', render_kw={'accept': 'image/*'}, validators=[Optional(), validators.regexp(u'([^\\s]+(\\.(?i)(jpe?g|png))$)')])
   password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
   password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])

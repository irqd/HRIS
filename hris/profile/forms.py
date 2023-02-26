from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, FileField, validators
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp, Optional)
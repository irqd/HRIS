from flask_wtf import FlaskForm
from wtforms import (EmailField, FileField, PasswordField, SubmitField,
                     validators)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length, Optional, Regexp, ValidationError)

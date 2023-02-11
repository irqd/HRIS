from flask_wtf import FlaskForm
import re
from wtforms import (FileField, PasswordField, StringField, SubmitField, SelectField, 
                     EmailField, DateField, validators, FormField, TimeField, TextAreaField, HiddenField)
from wtforms.validators import (DataRequired, Email, EqualTo,
                              Length, ValidationError, InputRequired, Regexp)

class DeleteEmployeeModal(FlaskForm):
   delete = SubmitField(label='Delete')


class AddEmployeeForm(FlaskForm):
   def validate_image(form, field):
      if field.data:
         field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

   #Employee Account
   image_path = FileField(label='Employee Picture', render_kw={'accept': 'image/*'},validators=[validators.regexp(u'([^\\s]+(\\.(?i)(jpe?g|png))$)')])
   company_email = EmailField(label='Company Email', validators=[DataRequired()])
   password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
   password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
   access = SelectField(label='Access', choices=[('admin', 'Admin'), ('employee', 'Employee')], 
   validators=[DataRequired()])

   #Employee Profile
   last_name = StringField(label='Last Name', validators=[DataRequired()])
   first_name = StringField(label='First Name', validators=[DataRequired()])
   middle_name = StringField(label='Middle Name', validators=[DataRequired()])
   gender = SelectField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
   validators=[DataRequired()])
   birth_date = StringField(label='Birth Date', validators=[DataRequired()])
   civil_status = SelectField(label='Civil Status', choices=[('single', 'Single'), ('married', 'Married'), 
   ('divorced', 'Divorced'), ('separated', 'Separated'), ('widowed', 'Widowed')], validators=[DataRequired()])
   mobile = StringField(label='Mobile Number', validators=[DataRequired()])
   email = EmailField(label='Email', validators=[DataRequired()])
   address = StringField(label='Address', validators=[DataRequired()])
   emergency_name = StringField(label='Contact Name', validators=[DataRequired()])
   emergency_contact = StringField(label='Contact Number', validators=[DataRequired()])
   emergency_relationship = StringField(label='Relationship', validators=[DataRequired()])
   tin = StringField(label='TIN', validators=[DataRequired(), Length(min=9, max=12)])
   sss = StringField(label='SSS', validators=[DataRequired(), Length(min=10, max=10)])
   phil_health = StringField(label='Philhealth', validators=[DataRequired(), Length(min=12, max=12)])
   pag_ibig = StringField(label='Pag-Ibig', validators=[DataRequired(), Length(min=12, max=12)])

   #Employment Info
   department = SelectField(label='Department' , coerce=int, validators=[DataRequired()], render_kw={'onchange': "changeOptions()"})
   positions = SelectField(label='Position', coerce=int, validators=[DataRequired()])
   description = TextAreaField(label='Description')
   salary_package = StringField(label='Salary Package', validators=[DataRequired()])
   start_date = StringField(label='Start Date', validators=[DataRequired()])
   end_date = StringField(label='End Date', render_kw={'disabled':True}, validators=[DataRequired()])
   status = SelectField(label='Status', choices=[('hired', 'Hired'), ('retired', 'Retired'), ('terminated', 'Terminated')])
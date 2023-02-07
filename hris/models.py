from . import db, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
import enum

@login_manager.user_loader
def load_user(user_id):
   return Users.query.get(int(user_id))

class USER_TYPES(enum.Enum):
      Employee = "Employee"
      Admin = "Admin"


class Users(db.Model, UserMixin):
   # Keys
   id = db.Column(db.Integer(), primary_key=True)  # Account_ID PK
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))  # Employee_ID FK
   email = db.Column(db.String(length=50), nullable=False, unique=True)
   
   #should have default values ('Admin', 'Employee')
   # access = db.Column(db.String(length=50), nullable=False, unique=True, default='employee')
   access = db.Column(db.Enum(USER_TYPES), nullable=False, unique=True, default=USER_TYPES.Employee)
   password_hash = db.Column(db.String(length=60), nullable=False)

   @property
   def password(self):
      return self.password

   # Encrypt password
   @password.setter
   def password(self, plain_text_password):
      self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

   def verify_password(self, attempted_password):
      return bcrypt.check_password_hash(self.password_hash, attempted_password)


class EmployeeInfo(db.Model):
   #Keys
   id = db.Column(db.Integer(), primary_key=True)

   first_name = db.Column(db.String(length=50), nullable=False)
   middle_name = db.Column(db.String(length=50), nullable=False)
   last_name = db.Column(db.String(length=50), nullable=False)
   gender = db.Column(db.String(length=50), nullable=False)
   birth_date= db.Column(db.DateTime(timezone=True), nullable=False)
   civil_status = db.Column(db.String(length=50), nullable=False)
   mobile = db.Column(db.String(length=50), nullable=False)
   email = db.Column(db.String(length=50), nullable=False)
   address = db.Column(db.String(length=50), nullable=False)
   emergency_name = db.Column(db.String(length=50), nullable=False)
   emergency_contact = db.Column(db.String(length=50), nullable=False)
   emergency_relationship = db.Column(db.String(length=50), nullable=False)
   tin = db.Column(db.String(length=50), nullable=False)
   SSS = db.Column(db.String(length=50), nullable=False)
   pag_ibig = db.Column(db.String(length=50), nullable=False)

      
   #Relationship
   user_info = db.relationship('Users')
   employment_info = db.relationship('EmploymentInfo')

class Attendance(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   date= db.Column(db.DateTime(timezone=True), nullable=False)
   first_in= db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   last_out= db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   
   #Relationship
   employee_info = db.relationship('EmploymentInfo')

class Leave(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   type = db.Column(db.String(length=50), nullable=False)
   start_date= db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   end_date= db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   status = db.Column(db.String(length=50), nullable=False)
   approved_by = db.Column(db.String(length=50), nullable=False)

   #Relationship
   employee_info = db.relationship('EmploymentInfo')

class EmploymentInfo(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   start_date= db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   end_date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
   status = db.Column(db.String(length=50), nullable=False)
   
   #Foreign Keys
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))
   attendance_id = db.Column(db.Integer(), db.ForeignKey('attendance.id'))
   leave_id = db.Column(db.Integer(), db.ForeignKey('leave.id'))
   position_id = db.Column(db.Integer(), db.ForeignKey('position.id'))

class Position(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   department_id = db.Column(db.Integer(), db.ForeignKey('department.id'))
   name = db.Column(db.String(length=50), nullable=False)
   description = db.Column(db.String(length=50), nullable=False)

   #Relationship
   employment_info = db.relationship('EmploymentInfo')

class Department(db.Model):
   id = db.Column(db.Integer(), primary_key=True)
   name = db.Column(db.String(length=50), nullable=False)
   description = db.Column(db.String(length=50), nullable=False)
   director = db.Column(db.String(length=50), nullable=False)

   #Relationship
   position = db.relationship('Position')
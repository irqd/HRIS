from . import db, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy
import enum

class USER_TYPES(enum.Enum):
   Employee = "Employee"
   Admin = "Admin"

class STATUS_TYPES(enum.Enum):
   Approved = "Approved"
   Declined = "Declined"
   Pending = "Pending"

class HIRE_TYPES(enum.Enum):
   Hired = "Hired"
   Retired = "Retired"
   Terminated = "Terminated"

class ATTENDANCE_TYPES(enum.Enum):
   Present = "Present"
   Absent = "Absent"
   Unavailable = "Unavailable"

class LEAVE_TYPES(enum.Enum):
   Sick_Leave = "Sick_Leave"
   SIL = "SIL"
   Maternity_Leave = "Maternity_Leave"
   Paternity_Leave = "Paternity_Leave"
   Vacation_Leave = "Vacation_Leave"
   Parental_Leave = "Parental_Leave"   
   Rehabilitation_Leave = "Rehabilitation_Leave"
   Study_Leave = "Study_Leave"

class POSITION_STATUS(enum.Enum):
   Hiring = "Hiring"
   Full = "Full"

@login_manager.user_loader
def load_user(user_id):
   return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
   # Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   name = db.Column(db.String(length=60), nullable=False)
   image_path = db.Column(db.String(length=50), server_default='images/profile.svg')
   company_email = db.Column(db.String(length=50), nullable=False, unique=True)
   password_hash = db.Column(db.String(length=60), nullable=False)
   access = db.Column(db.Enum(USER_TYPES), nullable=False, unique=True, default=USER_TYPES.Employee)
   date_created = db.Column(db.Date(), default=func.current_date(), nullable=False)

   # Foreign Keys
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))

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
   # Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   last_name = db.Column(db.String(length=50), nullable=False)
   first_name = db.Column(db.String(length=50), nullable=False)
   middle_name = db.Column(db.String(length=50), nullable=False)
   gender = db.Column(db.String(length=50), nullable=False)
   birth_date= db.Column(db.Date(), nullable=False)
   civil_status = db.Column(db.String(length=50), nullable=False)
   mobile = db.Column(db.String(length=50), nullable=False)
   email = db.Column(db.String(length=50), nullable=False)
   address = db.Column(db.String(length=50), nullable=False)
   emergency_name = db.Column(db.String(length=50), nullable=False)
   emergency_contact = db.Column(db.String(length=50), nullable=False)
   emergency_relationship = db.Column(db.String(length=50), nullable=False)
   tin = db.Column(db.String(length=50), nullable=False, unique=True)
   SSS = db.Column(db.String(length=50), nullable=False, unique=True)
   phil_health = db.Column(db.String(length=50), nullable=False, unique=True)
   pag_ibig = db.Column(db.String(length=50), nullable=False, unique=True)
   date_created = db.Column(db.Date(), default=func.current_date(), nullable=False)

   #Foreign Keys  
   position_id = db.Column(db.Integer(), db.ForeignKey('positions.id'))

   #Relationship
   user_info = db.relationship('Users', backref='employee_info')
   employment_info = db.relationship('EmploymentInfo', backref='employee_info')
   attendance_info = db.relationship('Attendance', backref='employee_info')
   leave_info = db.relationship('Leave', backref='employee_info')

   @hybrid_property
   def fullname(self):
      return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
   
   @hybrid_property
   def getEmployment(self):
      if self.employment_info:
         return self.employment_info
      else:
         return None
   
   

class EmploymentInfo(db.Model):
   #Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   description = db.Column(db.String(length=500))
   salary_package = db.Column(db.String(length=50), nullable=False)
   start_date= db.Column(db.Date(), nullable=False)
   end_date = db.Column(db.Date(), nullable=True)
   status = db.Column(db.Enum(HIRE_TYPES), nullable=False, default=HIRE_TYPES.Hired)

   #Foreign Key
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))


class Attendance(db.Model):
   #Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   #shift
   date= db.Column(db.Date(), nullable=False)
   attendance_type = db.Column(db.Enum(ATTENDANCE_TYPES), default=ATTENDANCE_TYPES.Unavailable, nullable=False)
   status = db.Column(db.Enum(STATUS_TYPES), default=STATUS_TYPES.Pending, nullable=False)
   start_shift= db.Column(db.Time(), nullable=False)
   end_shift= db.Column(db.Time(), nullable=False)

   # Time
   checked_in= db.Column(db.Time(),  nullable=True)
   checked_out= db.Column(db.Time(), nullable=True)

   #todo pre-post ot 
   pre_ot= db.Column(db.Time(), nullable=False)
   post_ot= db.Column(db.Time(), nullable=True)

   #Foreign Keys  
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))

   @hybrid_property
   def total_hours(self):
      return (self.end_shift - self.start_shift).total_seconds() / 3600
      

class Leave(db.Model):
   #Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   type = db.Column(db.Enum(LEAVE_TYPES), default=LEAVE_TYPES.Sick_Leave, nullable=False)
   date_requested= db.Column(db.Date(), default=func.current_date(), nullable=False)
   start_date= db.Column(db.Date(), nullable=False)
   end_date= db.Column(db.Date(), nullable=False)
   status = db.Column(db.Enum(STATUS_TYPES),default=STATUS_TYPES.Pending, nullable=False)
   approved_date =db.Column(db.Date(), nullable=False)
   approved_by = db.Column(db.String(length=50), nullable=False)

   #Foreign Keys  
   employee_id = db.Column(db.Integer(), db.ForeignKey('employee_info.id'))

   
class Positions(db.Model):
   #Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   position_name = db.Column(db.String(length=50), nullable=False)
   description = db.Column(db.String(length=500))
   position_status = db.Column(db.Enum(POSITION_STATUS), default=POSITION_STATUS.Hiring, nullable=False)
   date_created= db.Column(db.Date(), default=func.current_date(), nullable=False)

   #Foreign Key
   department_id = db.Column(db.Integer(), db.ForeignKey('departments.id'))

   #Association Proxy
   dept_assigned = association_proxy('departments', 'department_name')

   def obj_to_dict(self):
      return {
         'id': self.id,
         'position_name': self.position_name,
         'department_id': self.department_id
      }

class Departments(db.Model):
   #Primary Key
   id = db.Column(db.Integer(), primary_key=True)

   department_name = db.Column(db.String(length=50), nullable=False)
   supervisor = db.Column(db.String(length=50))
   description = db.Column(db.String(length=500))
   date_created= db.Column(db.Date(), default=func.current_date(), nullable=False)

   #Relationship
   positions_info = db.relationship('Positions', backref='departments_info')

   def obj_to_dict(self):
      return {
         'id': self.id,
         'department_name': self.department_name,
      }
      
   @hybrid_property
   def getPositions(self):
      if self.positions_info:
         return self.positions_info
      else:
         return None
   

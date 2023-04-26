from hris import models as m
from hris import db
from sqlalchemy.sql import func

def create_default_data():
   department = m.Departments(
      department_name = 'Admin',
      manager = 'Admin',
      description = 'Admin Department',
      date_created = "2021-01-01",
   )

   db.session.add(department)
   db.session.flush()

   position = m.Positions(
      position_name = 'Admin',
      description = 'Admin Position',
      position_status = 'Full',
      date_created = func.current_date(),
      department_id = department.id
   )

   db.session.add(position)
   db.session.flush()

   salary = m.Salaries(
      salary_name = 'Admin',
      description = 'Admin Salary',
      daily_rate = 000,
      hourly_rate = 000,
      bir_tax = 000,
      sss_tax = 000,
      phil_health_tax = 000,
      pag_ibig_tax = 000,
      ot_rate = 000,
      allowance = 000,
   )

   db.session.add(salary)
   db.session.flush()

   admin = m.EmployeeInfo(
      last_name = 'Admin',
      first_name = 'Admin',
      middle_name = 'Admin',
      gender = 'Male',
      birth_date = '2001-01-01',
      civil_status = 'Single',
      mobile = '09123456789',
      email = 'admin@email.com',
      address = 'None',
      emergency_name = 'None',
      emergency_contact = 'None',
      emergency_relationship = 'None',
      tin = '000000000000',
      sss = '0000000000',
      phil_health = '000000000000',
      pag_ibig = '000000000000',
      date_created = func.current_date(),
      position_id = position.id
   )

   db.session.add(admin)
   db.session.flush()

   admin_employment = m.EmploymentInfo(
      description = 'Admin',
      start_date = func.current_date(),
      status = 'Hired',
      employee_id = admin.id,
      salary_id = salary.id
   )

   db.session.add(admin_employment)
   db.session.flush()

   admin_user = m.Users(
      name = 'Admin',
      company_email = 'admin@email.com',
      password_hash = '$2b$12$fR4Yp3GE.RAXxA5aNOXXVuMW7CQd01tKG.y.PMP4DcdLQMVjij7ny',
      access = 'Admin',
      date_created = func.current_date(),
      employee_id = admin.id
   )

   db.session.add(admin_user)
   db.session.commit()
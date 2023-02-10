from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from hris.models import *
from .forms import *

employees_bp = Blueprint('employees_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@employees_bp.route('/employees', methods=['GET'])
def employees():
   delete_modal = DeleteModal()
   employees = db.session.query(EmployeeInfo.id, EmployeeInfo.last_name, EmployeeInfo.first_name, 
      EmployeeInfo.middle_name, Positions.position_name, Departments.department_name, 
      EmploymentInfo.start_date, EmploymentInfo.salary_package)\
      .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
      .join(Positions, Positions.id == EmployeeInfo.position_id)\
      .join(Departments, Departments.id == Positions.department_id).all()

   return render_template('employees.html', employees=employees, delete_modal = delete_modal)

@employees_bp.route('/employees/add_employee', methods=['GET', 'POST'])
def add_employee():
   
   return render_template('add_employee.html')


@employees_bp.route('/employees/<string:employee_name>_<int:employee_id>', methods=['GET', 'POST'])
def manage_employee(employee_name, employee_id):

   return render_template('manage_employee.html', employee_name=employee_name, employee_id=employee_id)

@employees_bp.route('/employees/delete/<int:employee_id>', methods=['GET', 'POST'])
def delete_employee(employee_id):

   employees = db.session.query()\
      .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
      .join(Positions, Positions.id == EmployeeInfo.position_id)\
      .join(Departments, Departments.id == Positions.department_id)\
      .filter(EmployeeInfo.id == employee_id).delete()
   db.session.commit()

   return redirect(url_for('employees_bp.employees'))
   #return render_template('employees.html')
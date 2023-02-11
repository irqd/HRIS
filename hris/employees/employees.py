from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from hris.models import *
from .forms import *

employees_bp = Blueprint('employees_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@employees_bp.route('/employees', methods=['GET'])
def employees():
   delete_employee_modal = DeleteEmployeeModal()
   employees = db.session.query(EmployeeInfo.id, EmployeeInfo.last_name, EmployeeInfo.first_name, 
      EmployeeInfo.middle_name, Positions.position_name, Departments.department_name, 
      EmploymentInfo.start_date, EmploymentInfo.salary_package)\
      .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
      .join(Positions, Positions.id == EmployeeInfo.position_id)\
      .join(Departments, Departments.id == Positions.department_id).all()

   return render_template('employees.html', employees=employees, 
                                          delete_employee_modal=delete_employee_modal)


@employees_bp.route('/employees/add_employee', methods=['GET', 'POST'])
def add_employee():
   def dict_helper(obj_list):
      results = [item.obj_to_dict() for item in obj_list]
      return results

   # Queries
   departments = db.session.query(Departments).all()   
   positions = db.session.query(Positions).all()

   # Setting choices in from
   department_list = [(i.id, i.department_name) for i in departments]
   position_list = [(i.id, i.position_name) for i in positions]

   # Applying choices in form
   add_employee = AddEmployeeForm()
   add_employee.department.choices = department_list
   add_employee.positions.choices = position_list

   # Converting sql alchemy obj
   departments_list = dict_helper(departments)
   positions_list = dict_helper(positions)

   if request.method == 'POST':
      flash('Employee record submitted!', category='success')
      return redirect(url_for('employees_bp.employees'))

   return render_template('add_employee.html',add_employee=add_employee, 
                                             departments_list=departments_list,
                                             positions_list=positions_list)


@employees_bp.route('/employees/<int:employee_id>-<string:employee_name>', methods=['GET', 'POST'])
def manage_employee(employee_name, employee_id):
   # employee = db.session.query()\
   #        .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
   #        .join(Positions, Positions.id == EmployeeInfo.position_id)\
   #        .join(Departments, Departments.id == Positions.department_id)\
   #        .filter(EmployeeInfo.id == employee_id).first()
   #_employee_name = employee["EmployeeInfo"].full_name

   return render_template('manage_employee.html', employee_name=employee_name, employee_id=employee_id)

@employees_bp.route('/employees/delete_employee/<int:employee_id>', methods=['GET', 'POST'])
def delete_employee(employee_id):
   if request.method == 'POST':
      # employees = db.session.query()\
      #    .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
      #    .join(Positions, Positions.id == EmployeeInfo.position_id)\
      #    .join(Departments, Departments.id == Positions.department_id)\
      #    .filter(EmployeeInfo.id == employee_id).delete()
      # db.session.commit()
      flash('User deleted!', category='danger')
      return redirect(url_for('employees_bp.employees'))

   return render_template('employees.html')
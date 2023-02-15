from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from hris.models import *
from .forms import *

employees_bp = Blueprint('employees_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@employees_bp.route('/employees/get_positions')
def get_positions():
    department_id = request.args.get('department_id')
    positions = Positions.query.filter_by(department_id=department_id).all()
    positions = [{'id': position.id, 'name': position.position_name} for position in positions]
    return jsonify(positions)


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
   add_employee = EmployeeForm()
   departments = db.session.query(Departments).all()   
   
   if request.method == 'POST':
      flash('Employee record submitted!', category='success')
      return redirect(url_for('employees_bp.employees'))

   return render_template('add_employee.html',add_employee=add_employee, 
                                             departments=departments)


@employees_bp.route('/employees/<int:employee_id>-<string:employee_name>', methods=['GET', 'POST'])
def manage_employee(employee_name, employee_id):
   selected_employee = db.session.query(Users, EmployeeInfo, EmploymentInfo, Positions, Departments)\
      .join(EmploymentInfo).join(Users).join(Positions).join(Departments)\
      .filter(EmployeeInfo.id == employee_id).first()

   user, employee_info, employment_info, position, department = selected_employee
   
   departments = db.session.query(Departments).all() 
   positions = department.getPositions

   manage_employee = EmployeeForm(
      #users
      image_path = user.image_path,
      company_email = user.company_email,
      access = user.access.value,
      
      #employee info
      last_name = employee_info.last_name,
      first_name = employee_info.first_name,
      middle_name = employee_info.middle_name,
      gender = employee_info.gender,
      birth_date = employee_info.birth_date,
      civil_status = employee_info.civil_status,
      mobile = employee_info.mobile,
      email = employee_info.email,
      address = employee_info.address,
      tin = employee_info.tin,
      sss = employee_info.SSS,
      phil_health = employee_info.phil_health,
      pag_ibig = employee_info.pag_ibig,
      emergency_name = employee_info.emergency_name,
      emergency_contact = employee_info.emergency_contact,
      emergency_relationship = employee_info.emergency_relationship,

   
      #Employment Profile
      description = employment_info.description,
      salary_package = employment_info.salary_package,
      start_date = employment_info.start_date,
      end_date = employment_info.end_date,
      status = employment_info.status.value,
      position = employee_info.position_id
      
   )

   department_id = position.department_id

   if request.method == 'POST':
      flash(f"{employee_info.fullname}'s profile updated successfully", category='success')
      return redirect(url_for('employees_bp.employees'))

   return render_template('manage_employee.html', manage_employee=manage_employee,
                                                   departments=departments,
                                                   positions=positions,
                                                   department_id=department_id,
                                                   employee_info=employee_info)

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
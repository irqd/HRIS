from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, current_app
from flask_login import current_user, login_required
from hris.models import *
from .forms import *
from werkzeug.utils import secure_filename
import os 

employees_bp = Blueprint('employees_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='employee/static')

@employees_bp.route('/employees/get_positions')
@login_required
def get_positions():
    department_id = request.args.get('department_id')
    positions = Positions.query.filter_by(department_id=department_id).all()
    positions = [{'id': position.id, 'name': position.position_name} for position in positions]
    return jsonify(positions)


@employees_bp.route('/employees', methods=['GET'])
@login_required
def employees():
   delete_employee_modal = DeleteEmployeeModal()

   employees = db.session.query(EmployeeInfo.id, EmployeeInfo.last_name, EmployeeInfo.first_name, 
      EmployeeInfo.middle_name, Positions.position_name, Departments.department_name, 
      EmploymentInfo.start_date, EmploymentInfo.salary_id, EmploymentInfo.status, Salaries.amount)\
      .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
      .join(Positions, Positions.id == EmployeeInfo.position_id)\
      .join(Departments, Departments.id == Positions.department_id)\
      .join(Salaries, Salaries.id == EmploymentInfo.salary_id).all()
      
   return render_template('employees.html', employees=employees, 
                                          delete_employee_modal=delete_employee_modal)


@employees_bp.route('/employees/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():  
   add_employee = EmployeeForm()
   
   departments = db.session.query(Departments).all()   
   salaries = db.session.query(Salaries).all()

   if request.method == 'POST':
      
      if add_employee.validate_on_submit:
            
         new_employee_info = EmployeeInfo(
            last_name = add_employee.last_name.data,
            first_name = add_employee.first_name.data,
            middle_name = add_employee.middle_name.data,
            gender = add_employee.gender.data,
            birth_date = datetime.strptime(add_employee.birth_date.data, '%Y-%m-%d').date(),
            civil_status = add_employee.civil_status.data,
            mobile = add_employee.mobile.data,
            email = add_employee.email.data,
            address = add_employee.address.data,
            emergency_name = add_employee.emergency_name.data,
            emergency_contact = add_employee.emergency_contact.data,
            emergency_relationship = add_employee.emergency_relationship.data,
            tin = add_employee.tin.data,
            SSS = add_employee.sss.data,
            phil_health = add_employee.phil_health.data,
            pag_ibig = add_employee.pag_ibig.data,
            position_id = add_employee.positions.data
         )

         db.session.add(new_employee_info)
         db.session.flush()

         new_employment_info = EmploymentInfo(
            description = add_employee.description.data,
            start_date = datetime.strptime(add_employee.start_date.data, '%Y-%m-%d').date(),
            status = add_employee.status.data,
            employee_id = new_employee_info.id,
            salary_id = add_employee.salary_rate.data
         )

         db.session.add(new_employment_info)
         db.session.flush()

         new_employee_account = Users(
            name = new_employee_info.fullname,
            company_email = add_employee.company_email.data,
            password = add_employee.password1.data,
            employee_id = new_employee_info.id
         )

         file = request.files['image_path']

         if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)
         
            rel_path = os.path.join('images', 'uploads', filename).replace('\\', '/')
            new_employee_account.image_path = rel_path
         
         db.session.add(new_employee_account)
         db.session.commit()

         flash('Employee record submitted!', category='success')
         return redirect(url_for('employees_bp.employees'))

   return render_template('add_employee.html',add_employee=add_employee, 
                                             departments=departments,
                                             salaries=salaries)


@employees_bp.route('/employees/<int:employee_id>-<string:employee_name>', methods=['GET', 'POST'])
@login_required
def manage_employee(employee_name, employee_id):
   selected_employee = db.session.query(Users, EmployeeInfo, EmploymentInfo, Positions, Departments)\
      .join(EmploymentInfo).join(Users).join(Positions).join(Departments)\
      .filter(EmployeeInfo.id == employee_id).first()

   user, employee_info, employment_info, position, department = selected_employee
   
   departments = db.session.query(Departments).all() 
   salaries = db.session.query(Salaries).all()
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
      salary_rate = employment_info.salary_id,
      start_date = employment_info.start_date,
      end_date = employment_info.end_date,
      status = employment_info.status.value,
      positions = employee_info.position_id
      
   )

   department_id = position.department_id
   position_id = employee_info.position_id

   if request.method == 'POST':

      if manage_employee.validate_on_submit:
         user.company_email = manage_employee.company_email.data
         user.access = manage_employee.access.data
         #user.password = manage_employee.password1,

         employee_info.last_name = manage_employee.last_name.data
         employee_info.first_name = manage_employee.first_name.data
         employee_info.middle_name = manage_employee.middle_name.data
         employee_info.gender = manage_employee.gender.data
         employee_info.birth_date = manage_employee.birth_date.data
         employee_info.civil_status = manage_employee.civil_status.data
         employee_info.mobile = manage_employee.mobile.data
         employee_info.email = manage_employee.email.data
         employee_info.address = manage_employee.address.data
         employee_info.tin = manage_employee.tin.data
         employee_info.sss = manage_employee.sss.data
         employee_info.phil_health = manage_employee.phil_health.data
         employee_info.pag_ibig = manage_employee.pag_ibig.data
         employee_info.emergency_name = manage_employee.emergency_name.data
         employee_info.emergency_contact = manage_employee.emergency_contact.data
         employee_info.emergency_relationship = manage_employee.emergency_relationship.data
         employee_info.position = manage_employee.positions.data

         employment_info.description = manage_employee.description.data
         employment_info.salary_id = manage_employee.salary_rate.data
         employment_info.start_date = manage_employee.start_date.data
         employment_info.end_date = None if manage_employee.status.data == 'hired' else manage_employee.end_date.data
         employment_info.status = manage_employee.status.data

         file = request.files['image_path']

         if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)
         
            rel_path = os.path.join('images', 'uploads', filename).replace('\\', '/')
            user.image_path = rel_path
   
         db.session.commit()
         flash(f"{employee_info.fullname}'s profile updated successfully", category='success')
         return redirect(url_for('employees_bp.employees'))

   return render_template('manage_employee.html', manage_employee=manage_employee,
                                                   departments=departments,
                                                   positions=positions,
                                                   department_id=department_id,
                                                   position_id=position_id, 
                                                   employee_info=employee_info,
                                                   user=user,
                                                   salaries=salaries)

@employees_bp.route('/employees/delete_employee/<int:employee_id>', methods=['GET', 'POST'])
@login_required
def delete_employee(employee_id):
   
   if request.method == 'POST':
      remove_employee = EmployeeInfo.query.filter_by(id = employee_id).delete()
      db.session.commit()
      flash('User deleted!', category='danger')
      return redirect(url_for('employees_bp.employees'))
   
   return render_template('employees.html')
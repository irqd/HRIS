from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required
from hris.employees.forms import *
from .forms import *
import os
from werkzeug.utils import secure_filename

profile_bp = Blueprint('profile_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='/profile_bp.static')



@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    selected_employee = db.session.query(Users, EmployeeInfo, EmploymentInfo, Positions, Departments)\
        .join(EmploymentInfo).join(Users).join(Positions).join(Departments)\
        .filter(EmployeeInfo.id == current_user.id).first()

    user, employee_info, employment_info, position, department = selected_employee

    employee_form = EmployeeForm(
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

    return render_template('profile.html', user=user,
                        employee_info=employee_info,
                        employment_info=employment_info,
                        position=position,
                        department=department,
                        employee_form=employee_form)

@profile_bp.route('/profile/<int:employee_id>/change_account/', methods=['GET', 'POST'])
@login_required
def account_settings(employee_id):
    selected_employee = Users.query.filter_by(id = current_user.id).first()
    account_form = AccountForm()
    return render_template('account_settings.html', selected_employee=selected_employee, account_form=account_form)


@profile_bp.route('/profile/<int:employee_id>/change_account/save_account', methods=['POST'])
@login_required
def save_account_settings(employee_id):
    
    if request.method == 'POST':
        account_form = AccountForm(request.form)
        attempted_password = account_form.password1.data

        user_account = Users.query.filter_by(id = employee_id).first()
        if account_form.validate_on_submit():
            #Upload
            file = request.files['image_path']
            
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                
                file.save(filepath)
               
                rel_path = os.path.join('images', 'uploads', filename).replace('\\', '/')
                user_account.image_path = rel_path

            if attempted_password and user_account.verify_password(attempted_password):
                flash("New password can't be the same as the old password.", category='danger')
                return redirect(url_for('profile_bp.profile'))
            else:
                user_account.password = attempted_password
                db.session.commit()
                
            flash(f'Updated Account', category='success')
        return redirect(url_for('profile_bp.profile'))
    
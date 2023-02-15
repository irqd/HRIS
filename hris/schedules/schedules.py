from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


schedules_bp = Blueprint('schedules_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@schedules_bp.route('/schedules', methods=['GET', 'POST'])
def schedules():
    employees = db.session.query(EmployeeInfo.id, EmployeeInfo.last_name, EmployeeInfo.first_name, 
    EmployeeInfo.middle_name, Positions.position_name, Departments.department_name,
    EmploymentInfo.status)\
    .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
    .join(Positions, Positions.id == EmployeeInfo.position_id)\
    .join(Departments, Departments.id == Positions.department_id).all()

    return render_template('schedules.html', employees=employees)

@schedules_bp.route('/schedules/manage_schedule/<int:employee_id>', methods=['GET', 'POST'])
def manage_schedule(employee_id):
    
    return render_template('manage_schedule.html')



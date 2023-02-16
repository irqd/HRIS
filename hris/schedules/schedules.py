from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .forms import *
from datetime import datetime, timedelta

schedules_bp = Blueprint('schedules_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='schedules/static')

@schedules_bp.route('/schedules', methods=['GET', 'POST'])
def schedules():
    employees = db.session.query(EmployeeInfo.id, EmployeeInfo.last_name, EmployeeInfo.first_name, 
    EmployeeInfo.middle_name, EmployeeInfo.fullname, Positions.position_name, Departments.department_name,
    EmploymentInfo.status)\
    .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
    .join(Positions, Positions.id == EmployeeInfo.position_id)\
    .join(Departments, Departments.id == Positions.department_id).all()

    return render_template('schedules.html', employees=employees)

@schedules_bp.route('/schedules/manage_schedule/<int:employee_id>/<string:employee_name>', methods=['GET', 'POST'])
def manage_schedule(employee_id, employee_name):
    add_schedule_modal = AddScheduleModal()
    edit_schedule_modal = EditScheduleModal()
    if request.method == 'POST':
        if add_schedule_modal.validate_on_submit():

            start_date = datetime.strptime(add_schedule_modal.start_date.data, '%Y-%m-%d')
            end_date = datetime.strptime(add_schedule_modal.end_date.data, '%Y-%m-%d')

            dates_in_between = []
            current_date = start_date

            while current_date <= end_date:
                if current_date.weekday() not in [5,6]:
                    dates_in_between.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)
               
            schedules_to_insert = []
            for date in dates_in_between:
                    schedules_to_insert.append({
                        'date' : date,
                        'start_shift' : add_schedule_modal.start_shift.data,
                        'end_shift' : add_schedule_modal.end_shift.data,
                        'employee_id' : employee_id
                    })
                
            db.session.bulk_insert_mappings(Attendance, schedules_to_insert)
            db.session.commit()
            
            flash('Schedule added!', category='success')
            return redirect(url_for('schedules_bp.manage_schedule', employee_id=employee_id, employee_name=employee_name))
        
    return render_template('manage_schedule.html', employee_id=employee_id, 
                                                add_schedule_modal=add_schedule_modal,
                                                employee_name=employee_name,
                                                edit_schedule_modal=edit_schedule_modal)


@schedules_bp.route('schedules/edit_schedule/<int:employee_id>/<string:employee_name>', methods=['POST'])
def edit_schedule(employee_id, employee_name):
    if request.method == 'POST':
        flash('Schedule edited!', category='warning')
        return redirect(url_for('schedules_bp.manage_schedule', employee_id=employee_id, employee_name=employee_name))

@schedules_bp.route('schedules/get_attendance', methods=['GET'])
def get_attendance():
    employee_id = request.args.get('employee_id')
    schedules = Attendance.query.filter_by(employee_id = employee_id).all()
    
    schedules = [{'id': schedule.id, 
                  'date': schedule.date.strftime("%y/%m/%d"), 
                  'attendance_type': schedule.attendance_type.value,
                  'status': schedule.status.value,
                  'start_shift': schedule.start_shift.isoformat(),
                  'end_shift': schedule.end_shift.isoformat(),
                  'employee_id':schedule.employee_id} for schedule in schedules]

    return jsonify(schedules)

from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .forms import *
from datetime import datetime, timedelta


attendance_bp = Blueprint('attendance_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='attendance/static')

@attendance_bp.route('attendance/get_attendance', methods=['GET'])
@login_required
def get_attendance():
    employee_id = request.args.get('employee_id')
    schedules = Attendance.query.filter_by(employee_id = current_user.employee_id).all()
    
    # loop through all schedules for the employee
    for schedule in schedules:
        start_shift_datetime = datetime.combine(schedule.date, schedule.start_shift)
        end_shift_datetime = datetime.combine(schedule.date, schedule.end_shift)

        # check if the current time is greater than the end shift time and the attendance type is not On Leave        
        if (datetime.now() > end_shift_datetime) and (schedule.attendance_type.value != 'On_Leave'):
            # check if the schedule has no check-in or check-out record
            if not schedule.checked_in and not schedule.checked_out:
                # mark attendance_type as Absent
                schedule.attendance_type = 'Absent'
                
    db.session.commit()

    schedules = [{'id': schedule.id,
                  'date': schedule.date.strftime("%y/%m/%d"),
                  'attendance_type': schedule.attendance_type.value,
                  'status': schedule.status.value,
                  'start_shift': schedule.start_shift.isoformat(),
                  'end_shift': schedule.end_shift.isoformat(),
                  'employee_id': schedule.employee_id} for schedule in schedules]
        
    return jsonify(schedules)

@attendance_bp.route('attendance/get_leave_requests', methods=['GET'])
@login_required
def get_leave_requests():
    employee_id = request.args.get('employee_id')
    leave_requests = Leave.query.filter_by(employee_id = current_user.employee_id).all()
    requests = [{'id': request.id, 
                  'type': request.type.value, 
                  'date_requested': request.date_requested.strftime("%y/%m/%d"),
                  'leave_date': request.leave_date.strftime("%y/%m/%d"),
                  'status': request.status.value,
                  'processed_date': request.processed_date.strftime("%y/%m/%d") if request.processed_date else '',
                  'processed_by' : request.processed_by,
                  'employee_id':request.employee_id} for request in leave_requests]

    return jsonify(requests)

@attendance_bp.route('/attendance', methods=['GET', 'POST'])
@login_required
def attendance():
    check_in = CheckInForm()
    check_out = CheckOutForm()
    request_leave = LeaveRequestForm()
    return render_template('attendance.html', check_in=check_in, check_out=check_out, request_leave=request_leave)

@attendance_bp.route('/attendance/check_in/<int:employee_id>', methods=['POST'])
def check_in(employee_id):
        
    if request.method == 'POST':
        schedule_id = request.form.get('schedule_id')
        attendance = Attendance.query.filter_by(id = schedule_id).first()

        check_in_time = datetime.strptime(request.form.get('check_in'), '%H:%M').time()        
        start_shift = attendance.start_shift

        # Convert time objects to datetime objects with a common date
        check_in_time_converted = datetime.combine(datetime.today(), check_in_time)
        start_shift_converted = datetime.combine(datetime.today(), start_shift)

        time_diff = check_in_time_converted - start_shift_converted 
    
        if time_diff > timedelta(minutes=15):
            attendance.attendance_type = 'Late'
            attendance.checked_in = check_in_time
            flash(f'You are: {str(abs(time_diff))} late', category='info')

        if check_in_time_converted <= start_shift_converted:
            attendance.attendance_type = 'Present'
            attendance.checked_in = check_in_time
            attendance.pre_ot = check_in_time
            flash(f'You are: {str(abs(time_diff))} early', category='info')

        db.session.commit()
  
        return redirect(url_for('attendance_bp.attendance'))

@attendance_bp.route('/attendance/check_out/<int:employee_id>', methods=['POST'])
def check_out(employee_id):
    if request.method == 'POST':
        schedule_id = request.form.get('schedule_id')
        attendance = Attendance.query.filter_by(id = schedule_id).first()
        # progress = attendance.get_progress
        check_out_time = datetime.strptime(request.form.get('check_out'), '%H:%M').time()        
        end_shift = attendance.end_shift
        
        # Convert time objects to datetime objects with a common date
        check_out_time_converted = datetime.combine(datetime.today(), check_out_time)
        end_shift_converted = datetime.combine(datetime.today(), end_shift) 

        time_diff = check_out_time_converted - end_shift_converted
        
        #OT
        if check_out_time_converted > end_shift_converted:
            attendance.checked_out = check_out_time
            attendance.post_ot = check_out_time
            flash(f"You've checked out with {str(abs(time_diff))} of overtime", category='info')

        # Early Out
        if check_out_time_converted < end_shift_converted:
            attendance.checked_out = check_out_time
            flash(f'You checked out: {str(abs(time_diff))} early', category='info')

        db.session.commit()
  
        return redirect(url_for('attendance_bp.attendance'))
    
@attendance_bp.route('/attendance/request_leave/<int:employee_id>', methods=['POST'])
def request_leave(employee_id):
    if request.method == 'POST':
        leave_request = LeaveRequestForm(request.form)
        if leave_request.validate_on_submit():
            
            start_date = datetime.strptime(leave_request.start_date.data, '%Y-%m-%d')
            end_date = datetime.strptime(leave_request.end_date.data, '%Y-%m-%d')

            dates_in_between = []
            current_date = start_date

            while current_date <= end_date:
                if current_date.weekday() not in [5,6]:
                    dates_in_between.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)
               
            leave_requests_to_insert = []   
            for date in dates_in_between:
                    leave_requests_to_insert.append({
                        'type' : leave_request.type.data,
                        'leave_date' : date,
                        'employee_id' : current_user.employee_id
                    })

            flash('Leave request submitted!', category='success')
            db.session.bulk_insert_mappings(Leave, leave_requests_to_insert)
            db.session.commit()

        return redirect(url_for('attendance_bp.attendance'))
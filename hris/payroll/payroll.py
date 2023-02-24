from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import or_, and_, func
from datetime import datetime, timedelta, date
import calendar


payroll_bp = Blueprint('payroll_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@payroll_bp.route('/payroll', methods=['GET'])
@login_required
def payroll():
    today = datetime.now()
    this_month = today.month

    first_day_of_month = datetime(today.year, this_month, 1).date()
    last_day_of_month = datetime(today.year, this_month, calendar.monthrange(today.year, this_month)[1]).date()

    first_cut_off = [str(first_day_of_month), None]
    second_cut_off = [None, str(last_day_of_month)]

    num_days_in_month = calendar.monthrange(today.year, this_month)[1]

    for day in range(1, num_days_in_month + 1):
        if day == 15:
            first_cut_off[1] = str(datetime(today.year, this_month, day).date())
        elif day == 16:
            second_cut_off[0] = str(datetime(today.year, this_month, day).date())


    return render_template('payroll.html', first_cut_off=first_cut_off, second_cut_off=second_cut_off)


@payroll_bp.route('/payroll/cut_off/<string:start_cut_off>/<string:end_cut_off>', methods=['GET'])
@login_required
def cut_off(start_cut_off, end_cut_off):

    employees = db.session.query(EmployeeInfo.id, EmployeeInfo.fullname, 
                EmploymentInfo.status, Salaries.daily_rate, Salaries.hourly_rate,
                Salaries.bir_tax, Salaries.sss_tax, Salaries.phil_health_tax, Salaries.pag_ibig_tax,
                Salaries.ot_rate, Salaries.allowance)\
                .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
                .join(Salaries, Salaries.id == EmploymentInfo.salary_id).all()
    
    employee_data = []
    for employee in employees: 

        result = Attendance.query.filter(Attendance.employee_id == employee.id)\
        .filter(Attendance.date.between(datetime.strptime(start_cut_off, '%Y-%m-%d'), datetime.strptime(end_cut_off, '%Y-%m-%d')))\
        .filter(or_(Attendance.attendance_type == 'Present', Attendance.attendance_type == 'Late'))\
        .filter(Attendance.status == STATUS_TYPES.Approved)

        #Calculate days present
        days_present = result.with_entities(func.count(Attendance.id)).scalar()

        #Calculate total regular and ot hours
        total_regular_hours = 0
        total_pre_ot_hours = 0
        total_post_ot_hours = 0
        for res in result:
            if res.total_regular_hours > 5.0:
                g = res.total_regular_hours - 1.0
                total_regular_hours += g

            if res.pre_ot_hours is not None:
                g = res.pre_ot_hours
                total_pre_ot_hours += g
            
            if res.post_ot_hours is not None:
                g = res.post_ot_hours
                total_post_ot_hours += g

        total_ot_hours = total_pre_ot_hours + total_post_ot_hours
        
        #Calculate gross pay
        gross_pay = (float(total_regular_hours) * float(employee.hourly_rate)) + (float(total_ot_hours) * float(employee.ot_rate))

        #Calculate deductions
        deductions = float(employee.bir_tax) + float(employee.sss_tax) + float(employee.phil_health_tax) + float(employee.pag_ibig_tax)
        
        #Calculate net pay
        net_pay = (gross_pay - deductions) + float(employee.allowance)
    
        data = {
            'employee_id': employee.id,
            'employee_name': employee.fullname,
            'image_path': 'test',
            'start_cut_off': start_cut_off,
            'end_cut_off': end_cut_off,
            'days_present': days_present,
            'total_regular_hours': total_regular_hours,
            'total_ot_hours': total_ot_hours,
            'gross_pay': gross_pay,
            'deductions': deductions,
            'allowance': float(employee.allowance),
            'net_pay': net_pay
        }
        
        employee_data.append(data)

    return render_template('cut_off.html', employee_data=employee_data)


@payroll_bp.route('/payroll/cut_off/<int:employee_id>/<string:start_cut_off>/<string:end_cut_off>', methods=['GET', 'POST'])
@login_required
def individual_payroll(employee_id, start_cut_off, end_cut_off):

    selected_employee = db.session.query(Users.image_path, Users.company_email, EmployeeInfo.id, EmployeeInfo.fullname, 
                    EmployeeInfo.mobile, EmploymentInfo.status, Salaries.daily_rate, Salaries.hourly_rate,
                    Salaries.bir_tax, Salaries.sss_tax, Salaries.phil_health_tax, Salaries.pag_ibig_tax,
                    Salaries.ot_rate, Salaries.allowance).filter(EmployeeInfo.id == employee_id)\
                    .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
                    .join(Users, Users.employee_id == employee_id)\
                    .join(Salaries, Salaries.id == EmploymentInfo.salary_id).first()
     
    employee_attendances = Attendance.query.filter(Attendance.employee_id == employee_id)\
        .filter(Attendance.date.between(datetime.strptime(start_cut_off, '%Y-%m-%d'), datetime.strptime(end_cut_off, '%Y-%m-%d')))\
        .filter(or_(Attendance.attendance_type == 'Present', Attendance.attendance_type == 'Late'))\
        .filter(Attendance.status == STATUS_TYPES.Approved)
    
    #Calculate days present
    days_present = employee_attendances.with_entities(func.count(Attendance.id)).scalar()

    #Calculate total hours
    total_regular_hours = 0
    total_pre_ot_hours = 0
    total_post_ot_hours = 0

    for res in employee_attendances:
        #print(res.total_regular_hours)
        if res.total_regular_hours > 5.0:
            g = res.total_regular_hours - 1.0
            total_regular_hours += g
    
        if res.pre_ot_hours is not None:
            g = res.pre_ot_hours
            total_pre_ot_hours += g

        if res.post_ot_hours is not None:
            g = res.post_ot_hours
            total_post_ot_hours += g
    
    total_ot_hours = total_pre_ot_hours + total_post_ot_hours

    #Calculate gross pay
    gross_pay = (float(total_regular_hours) * float(selected_employee.hourly_rate)) + (float(total_ot_hours) * float(selected_employee.ot_rate))

    #Calculate deductions
    deductions = float(selected_employee.bir_tax) + float(selected_employee.sss_tax) + float(selected_employee.phil_health_tax) + float(selected_employee.pag_ibig_tax)
    
    #Calculate net pay
    net_pay = (gross_pay - deductions) + float(selected_employee.allowance)

    data = {
        'employee_id': selected_employee.id,
        'employee_name': selected_employee.fullname,
        'image_path': selected_employee.image_path,
        'company_email': selected_employee.company_email,
        'mobile': selected_employee.mobile,
        'bir_tax': float(selected_employee.bir_tax),
        'sss_tax': float(selected_employee.sss_tax),
        'phil_health_tax': float(selected_employee.phil_health_tax),
        'pag_ibig_tax': float(selected_employee.pag_ibig_tax),
        'hourly_rate': float(selected_employee.hourly_rate),
        'ot_rate': float(selected_employee.ot_rate),
        'start_cut_off': start_cut_off,
        'end_cut_off': end_cut_off,
        'days_present': days_present,
        'total_regular_hours': total_regular_hours,
        'total_ot_hours': total_ot_hours,
        'gross_pay': gross_pay,
        'deductions': deductions,
        'allowance': float(selected_employee.allowance),
        'net_pay': net_pay
    }

    return render_template('individual_payroll.html', data=data)
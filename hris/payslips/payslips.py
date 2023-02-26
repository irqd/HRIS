from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response
from flask_login import login_required, current_user
from sqlalchemy import or_, and_
from hris.payroll import payroll
import pdfkit

payslips_bp = Blueprint('payslips_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='payslips/static')


def generate_payslip_data(employee_id, start_cut_off, end_cut_off):
    selected_employee = db.session.query(Users.image_path, Users.company_email, EmployeeInfo.id, 
    EmployeeInfo.fullname, EmployeeInfo.mobile, EmploymentInfo.status, Salaries.daily_rate, 
    Salaries.hourly_rate, Salaries.bir_tax, Salaries.sss_tax, Salaries.phil_health_tax, 
    Salaries.pag_ibig_tax, Salaries.ot_rate, Salaries.allowance).filter(EmployeeInfo.id == employee_id)\
    .join(EmployeeInfo, EmployeeInfo.id == EmploymentInfo.employee_id)\
    .join(Users, Users.employee_id == EmployeeInfo.id)\
    .join(Salaries, Salaries.id == EmploymentInfo.salary_id).first()
    
    employee_payslip = db.session.query(Payslips).filter(Payslips.employee_id == selected_employee.id)\
        .filter(Payslips.start_cut_off == start_cut_off).filter(Payslips.end_cut_off == end_cut_off).first()
    
    data = payroll.calculate_payroll(selected_employee, 
                            start_cut_off, 
                            end_cut_off,
                            total_regular_hours=float(employee_payslip.total_regular_hours),
                            total_pre_ot_hours=float(employee_payslip.pre_ot_hours),
                            total_post_ot_hours=float(employee_payslip.post_ot_hours),
                            allowance=float(employee_payslip.allowance))
    
    return data

@payslips_bp.route('/payslips', methods=['GET'])
@login_required
def payslips():
    employee_payslips = Payslips.query.filter(Payslips.employee_id == current_user.employee_id)\
    .filter(Payslips.status == 'Approved').all()
    
    return render_template('payslips.html', employee_payslips=employee_payslips)

@payslips_bp.route('/payslips/view_payslip/<string:start_cut_off>/<string:end_cut_off>', methods=['GET', 'POST'])
@login_required
def view_payslip(start_cut_off, end_cut_off):
    data = generate_payslip_data(current_user.employee_id, start_cut_off, end_cut_off)
    return render_template('view_payslip.html', data=data)

@payslips_bp.route('/payslips/download_payslip/<string:start_cut_off>/<string:end_cut_off>', methods=['GET', 'POST'])
@login_required
def download_payslip(start_cut_off, end_cut_off):

    config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf/bin/wkhtmltopdf.exe')
    #generate payslip data
    data = generate_payslip_data(current_user.employee_id, start_cut_off, end_cut_off)
    employee_name = data['employee_name']
    #generate template
    html = render_template('download_payslip.html', data=data)
    #convert template to pdf

    pdf = pdfkit.from_string(html, False, options={"enable-local-file-access": ""}, configuration=config)
    #pass pdf as response

    response = make_response(pdf)
    
    #set response headers
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={employee_name}_{start_cut_off}_{end_cut_off}.pdf'

    return response




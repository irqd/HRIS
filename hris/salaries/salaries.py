from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from .forms import *

salaries_bp = Blueprint('salaries_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='/salaries_bp.static')

@salaries_bp.route('/salaries', methods=['GET', 'POST'])
@login_required
def salaries():
    add_salary_modal = AddSalaryModal()
    delete_salary_modal = DeleteSalaryModal()
    edit_salary_modal = EditSalaryModal()
    salaries = Salaries.query.all()

    return render_template('salaries.html', salaries=salaries, 
                                            add_salary_modal=add_salary_modal,
                                            delete_salary_modal=delete_salary_modal,
                                            edit_salary_modal=edit_salary_modal
                                            )

@salaries_bp.route('/salaries/add_salary', methods=['POST'])
@login_required
def add_salary():
    add_salary_modal = AddSalaryModal(request.form)
    if request.method == 'POST':
        
        if add_salary_modal.validate_on_submit():
            salaries = Salaries(
                salary_name = add_salary_modal.salary_name.data,
                description = add_salary_modal.description.data,
                daily_rate = add_salary_modal.daily_rate.data,
                hourly_rate = add_salary_modal.hourly_rate.data,
                bir_tax = add_salary_modal.bir_tax.data,
                sss_tax = add_salary_modal.sss_tax.data,
                phil_health_tax = add_salary_modal.phil_health_tax.data,
                pag_ibig_tax = add_salary_modal.pag_ibig_tax.data,
                ot_rate = add_salary_modal.ot_rate.data,
                allowance = add_salary_modal.allowance.data
            )
            db.session.add(salaries)
            db.session.commit()
            flash('New Salary Added!', category='success')
        
        if add_salary_modal.errors != {}:
            for err in add_salary_modal.errors:
                flash(f'Error {err}', category='success')
        
    return redirect(url_for('salaries_bp.salaries'))


@salaries_bp.route('/salaries/<int:salary_id>/edit_salary', methods=['GET', 'POST'])
@login_required
def edit_salary(salary_id):
    edit_salary_modal = EditSalaryModal(request.form)

    if request.method == 'POST':
        if edit_salary_modal.validate_on_submit():

            salaries = Salaries.query.filter_by(id = salary_id).first()

            salaries.salary_name = edit_salary_modal.salary_name.data
            salaries.description = edit_salary_modal.description.data
            salaries.daily_rate = edit_salary_modal.daily_rate.data
            salaries.hourly_rate = edit_salary_modal.hourly_rate.data
            salaries.bir_tax = edit_salary_modal.bir_tax.data,
            salaries.sss_tax = edit_salary_modal.sss_tax.data,
            salaries.phil_health_tax = edit_salary_modal.phil_health_tax.data,
            salaries.pag_ibig_tax = edit_salary_modal.pag_ibig_tax.data,
            salaries.ot_rate = edit_salary_modal.ot_rate.data,
            salaries.allowance = edit_salary_modal.allowance.data

            db.session.commit()
            flash(f'{salaries.salary_name} Edited!', category='warning')

        if edit_salary_modal.errors != {}:
            for err_msg in edit_salary_modal.errors.values():
                flash(f'There is an error: {edit_salary_modal.errors}', category='danger')
        
    return redirect(url_for('salaries_bp.salaries', edit_salary_modal=edit_salary_modal))


@salaries_bp.route('/salaries/<int:salary_id>/delete_salary', methods=['GET', 'POST'])
@login_required
def delete_salary(salary_id):
    if request.method == 'POST':
        salaries = Salaries.query.filter_by(id = salary_id).delete()
        db.session.commit()
        
        flash('Salary Deleted!', category='danger')
    return redirect(url_for('salaries_bp.salaries'))
   
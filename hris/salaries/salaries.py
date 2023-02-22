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
    print(salaries)
    for salary in salaries:
        print(salary.id)
        print(salary.salary_name)
    return render_template('salaries.html', salaries=salaries, 
                                            add_salary_modal=add_salary_modal,
                                            delete_salary_modal=delete_salary_modal,
                                            edit_salary_modal=edit_salary_modal
                                            )

@salaries_bp.route('/salaries/add_salary', methods=['GET', 'POST'])
@login_required
def add_salary():
    add_salary_modal = AddSalaryModal(request.form)
    if request.method == 'POST':
        if add_salary_modal.validate_on_submit():
            salaries = Salaries(
                salary_name = add_salary_modal.salary_name.data,
                description = add_salary_modal.description.data,
                amount = add_salary_modal.amount.data,
                per_hour = add_salary_modal.per_hour.data,
            )
            db.session.add(salaries)
            db.session.commit()
            flash('add success', category='success')
        
    return redirect(url_for('salaries_bp.salaries'))


@salaries_bp.route('/salaries/<int:salary_id>/edit_salary', methods=['GET', 'POST'])
@login_required
def edit_salary(salary_id):

    edit_salary_modal = AddSalaryModal(request.form)
    if request.method == 'POST':
        if edit_salary_modal.validate_on_submit():

            salaries = Salaries.query.filter_by(id = salary_id).first()

            salaries.salary_name = edit_salary_modal.salary_name.data
            salaries.description = edit_salary_modal.description.data
            salaries.amount = edit_salary_modal.amount.data
            salaries.per_hour = edit_salary_modal.per_hour.data

            db.session.commit()
            flash('edit success', category='success')
        
    return redirect(url_for('salaries_bp.salaries'))


@salaries_bp.route('/salaries/<int:salary_id>/delete_salary', methods=['GET', 'POST'])
@login_required
def delete_salary(salary_id):
    if request.method == 'POST':
        salaries = Salaries.query.filter_by(id = salary_id).delete()
        db.session.commit()
        
        flash('success', category='success')
    return redirect(url_for('salaries_bp.salaries'))
   
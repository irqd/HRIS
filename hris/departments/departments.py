from flask import Blueprint, render_template, request, flash, redirect, url_for
from hris.models import *
from .forms import *

departments_bp = Blueprint('departments_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@departments_bp.route('/departments', methods=['GET', 'POST'])
def departments():
    delete_department_modal = DeleteDepartmentModal()
    departments = Departments.query.all()

    return render_template('departments.html', departments=departments,
                                            delete_department_modal=delete_department_modal)


@departments_bp.route('/departments/add_department', methods=['GET', 'POST'])
def add_department():
    return render_template('add_department.html')

@departments_bp.route('/departments/manage_department', methods=['GET', 'POST'])
def manage_department():
    return render_template('manage_department.html')

@departments_bp.route('/departments/delete_department/<int:department_id>', methods=['GET', 'POST'])
def delete_department(department_id):
    if request.method == 'POST':
        flash('Department deleted!', category='danger')
        return redirect(url_for('departments_bp.departments'))

    return render_template('departments.html')
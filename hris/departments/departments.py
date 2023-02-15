from flask import Blueprint, render_template, request, flash, redirect, url_for
from hris.models import *
from .forms import *

departments_bp = Blueprint('departments_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

# Department
@departments_bp.route('/departments', methods=['GET', 'POST'])
def departments():
    delete_department_modal = DeleteDepartmentModal()
    departments = Departments.query.all()

    return render_template('departments.html', departments=departments,
                                            delete_department_modal=delete_department_modal)


@departments_bp.route('/departments/add_department', methods=['GET', 'POST'])
def add_department():
    add_department = DepartmentForm()

    if request.method == 'POST':
        flash(f'{add_department.department_name.data} added successfully', category='success')
        return redirect(url_for('departments_bp.departments'))

    return render_template('add_department.html', add_department=add_department)
    

@departments_bp.route('/departments/manage_department/<int:department_id>', methods=['GET', 'POST'])
def manage_department(department_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    positions = selected_department.getPositions

    manage_department = DepartmentForm(
        department_name = selected_department.department_name,
        supervisor = selected_department.supervisor,
        description = selected_department.description
    )
    delete_position_modal = DeletePositionModal()

    if request.method == 'POST':
        flash(f'{manage_department.department_name.data} updated successfully', category='success')
        return redirect(url_for('departments_bp.departments'))

    return render_template('manage_department.html', manage_department=manage_department,
                                                    selected_department=selected_department,
                                                    positions=positions, delete_position_modal=delete_position_modal)
 

@departments_bp.route('/departments/delete_department/<int:department_id>', methods=['GET', 'POST'])
def delete_department(department_id):
    if request.method == 'POST':
        flash('Department deleted!', category='danger')
        return redirect(url_for('departments_bp.departments'))

    return render_template('departments.html')


# Position
@departments_bp.route('/departments/manage_department/<int:department_id>/add_position', methods=['GET', 'POST'])
def add_position(department_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    add_position = PositionForm()

    if request.method == 'POST':
        flash(f'{add_position.position_name.data} added successfully', category='success')
        return redirect(url_for('departments_bp.manage_department', department_id=department_id))

    return render_template('add_position.html', selected_department=selected_department, add_position=add_position)

@departments_bp.route('/departments/manage_department/<int:department_id>/manage_position/<int:position_id>', methods=['GET', 'POST'])
def manage_position(department_id, position_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    selected_position = Positions.query.filter_by(id = position_id).first()

    manage_position = PositionForm(
        position_name = selected_position.position_name,
        position_status = selected_position.position_status,
        description = selected_position.description
    )

    if request.method == 'POST':
        flash(f'{manage_position.position_name.data} updated successfully', category='success')
        return redirect(url_for('departments_bp.manage_department', department_id=department_id))

    return render_template('manage_position.html', selected_department=selected_department, manage_position=manage_position)

@departments_bp.route('/departments/manage_department/<int:department_id>/delete_position/<int:position_id>', methods=['GET', 'POST'])
def delete_position(department_id, position_id):
    if request.method == 'POST':
        flash(f'Position id: {position_id} deleted!', category='danger')
        return redirect(url_for('departments_bp.manage_department', department_id=department_id))

    return redirect(url_for('departments_bp.manage_department', department_id=department_id))





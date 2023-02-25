from flask import Blueprint, render_template, request, flash, redirect, url_for
from hris.models import *
from .forms import *
from flask_login import login_required
import sqlalchemy.exc as exc

departments_bp = Blueprint('departments_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

# Department
@departments_bp.route('/departments', methods=['GET', 'POST'])
@login_required
def departments():
    delete_department_modal = DeleteDepartmentModal()
    departments = Departments.query.all()

    return render_template('departments.html', departments=departments,
                                            delete_department_modal=delete_department_modal)


@departments_bp.route('/departments/add_department', methods=['GET', 'POST'])
@login_required
def add_department():
    add_department = DepartmentForm()

    # supervisors = db.session.query(EmployeeInfo.fullname, Positions.position_name, 
    #     Departments.department_name).join(EmployeeInfo, EmployeeInfo.position_id == Positions.id)\
    #     .join(Departments, Positions.department_id == Departments.id).all()
    
    if request.method == 'POST':
        if add_department.validate_on_submit():
            new_department = Departments(
                department_name = add_department.department_name.data,
                supervisor = add_department.supervisor.data,
                description = add_department.description.data
            )

            db.session.add(new_department)
            db.session.commit()

            flash(f'{add_department.department_name.data} added successfully', category='success')
            return redirect(url_for('departments_bp.departments'))

    return render_template('add_department.html', add_department=add_department)
    

@departments_bp.route('/departments/manage_department/<int:department_id>', methods=['GET', 'POST'])
@login_required
def manage_department(department_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    positions = selected_department.getPositions

    delete_position_modal = DeletePositionModal()
    manage_department = DepartmentForm(
        department_name = selected_department.department_name,
        supervisor = selected_department.supervisor,
        description = selected_department.description
    )

    if request.method == 'POST':
        if manage_department.validate_on_submit:
            selected_department.department_name = manage_department.department_name.data
            selected_department.supervisor = manage_department.supervisor.data if manage_department.supervisor.data else selected_department.supervisor
            selected_department.description = manage_department.description.data

            db.session.commit()

            flash(f'{manage_department.department_name.data} updated successfully', category='success')
            return redirect(url_for('departments_bp.departments'))

    return render_template('manage_department.html', manage_department=manage_department,
                                                    selected_department=selected_department,
                                                    positions=positions, delete_position_modal=delete_position_modal)
 

@departments_bp.route('/departments/delete_department/<int:department_id>', methods=['GET', 'POST'])
@login_required
def delete_department(department_id):
    if request.method == 'POST':

        try:
            department = Departments.query.filter_by(id = department_id).delete()
            db.session.commit()

            flash("Department deleted!", category='success')
            return redirect(url_for('departments_bp.departments'))
        except exc.IntegrityError:
            flash("This department has employees hired, can't proceed deletion!", category='warning')
            return redirect(url_for('departments_bp.departments'))
            
    #return render_template('departments.html')


# Position
@departments_bp.route('/departments/manage_department/<int:department_id>/add_position', methods=['GET', 'POST'])
@login_required
def add_position(department_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    add_position = PositionForm()

    if request.method == 'POST':
        if add_position.validate_on_submit:
            new_position = Positions(
                position_name = add_position.position_name.data,
                description = add_position.description.data,
                position_status = add_position.position_status.data,
                department_id = department_id
            )

            db.session.add(new_position)
            db.session.commit(  )

            flash(f'{add_position.position_name.data} added successfully', category='success')
            return redirect(url_for('departments_bp.manage_department', department_id=department_id))

    return render_template('/positions/add_position.html', selected_department=selected_department, add_position=add_position)


@departments_bp.route('/departments/manage_department/<int:department_id>/manage_position/<int:position_id>', methods=['GET', 'POST'])
@login_required
def manage_position(department_id, position_id):
    selected_department = Departments.query.filter_by(id = department_id).first()
    selected_position = Positions.query.filter_by(id = position_id).first()

    manage_position = PositionForm(
        position_name = selected_position.position_name,
        position_status = selected_position.position_status.value,
        description = selected_position.description
    )
    
    if request.method == 'POST':
        if manage_position.validate_on_submit:
            selected_position.position_name = manage_position.position_name.data
            selected_position.position_status = manage_position.position_status.data
            selected_position.description = manage_position.description.data

            db.session.commit()


            flash(f'{manage_position.position_name.data} updated successfully', category='success')
            return redirect(url_for('departments_bp.manage_department', department_id=department_id))

    return render_template('/positions/manage_position.html', selected_department=selected_department, manage_position=manage_position)


@departments_bp.route('/departments/manage_department/<int:department_id>/delete_position/<int:position_id>', methods=['GET', 'POST'])
@login_required
def delete_position(department_id, position_id):
    if request.method == 'POST':

        try:
            position = Positions.query.filter_by(id = request.form.get('position_id')).delete()
            db.session.commit()

            flash(f'Position deleted!', category='danger')
            return redirect(url_for('departments_bp.manage_department', department_id=department_id))
        except exc.IntegrityError:
            flash("This position has employees hired, can't proceed deletion!", category='warning')
            return redirect(url_for('departments_bp.manage_department', department_id=department_id))





from flask import Blueprint, render_template, request, flash, redirect, url_for
from hris.models import *

departments_bp = Blueprint('departments_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@departments_bp.route('/departments', methods=['GET', 'POST'])
def departments():
   departments = Departments.query.all()
   return render_template('departments.html', departments=departments)
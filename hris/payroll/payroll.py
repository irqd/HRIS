from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


payroll_bp = Blueprint('payroll_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@payroll_bp.route('/payroll', methods=['GET', 'POST'])
def payroll():
   return render_template('payroll.html')
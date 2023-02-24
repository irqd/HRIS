from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import or_, and_


payslips_bp = Blueprint('payslips_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@payslips_bp.route('/payslips', methods=['GET', 'POST'])
@login_required
def payslips():

    #TODO Attendance, employment, employee info, user?
    #kapag ang checked out lagpas na 5hrs kaltas 1hr para sa lunch

    return render_template('payslips.html')
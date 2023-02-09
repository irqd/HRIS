from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


attendance_bp = Blueprint('attendance_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@attendance_bp.route('/attendance', methods=['GET', 'POST'])
def attendance():
   return render_template('attendance.html')
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from hris.models import *
from sqlalchemy import or_
from collections import Counter

home_bp = Blueprint('home_bp', __name__, template_folder='templates',
    static_folder='static', static_url_path='static')


@home_bp.route('/', methods=['GET', 'POST'])
@home_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    
    attendances = Attendance.query.filter(Attendance.date == func.now()) \
    .filter(or_(Attendance.attendance_type == ATTENDANCE_TYPES.Absent.value, 
                Attendance.attendance_type == ATTENDANCE_TYPES.Present.value, 
                Attendance.attendance_type == ATTENDANCE_TYPES.Late.value, 
                Attendance.attendance_type == ATTENDANCE_TYPES.On_Leave.value)) \
    .all()

    attendance_counts = Counter([attendance.attendance_type for attendance in attendances])
    
    statistics = [attendance_counts[ATTENDANCE_TYPES.Present.value], 
              attendance_counts[ATTENDANCE_TYPES.Absent.value], 
              attendance_counts[ATTENDANCE_TYPES.Late.value], 
              attendance_counts[ATTENDANCE_TYPES.On_Leave.value]]

    print(statistics)
    return render_template('home.html', statistics=statistics)













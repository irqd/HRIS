from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
   return render_template('nav_contents/nav_contents_home.html')

@views.route('/personal_data', methods=['GET', 'POST'])
def personal_data():
   return render_template('nav_contents/personal_data.html')

@views.route('/attendance', methods=['GET', 'POST'])
def attendance():
   return render_template('nav_contents/attendance.html')

@views.route('/payroll', methods=['GET', 'POST'])
def payroll():
   return render_template('nav_contents/payroll.html')

@views.route('/employees', methods=['GET', 'POST'])
def employees():
   return render_template('nav_contents/employees.html')

@views.route('/departments', methods=['GET', 'POST'])
def departments():
   return render_template('nav_contents/departments.html')

@views.route('/schedules', methods=['GET', 'POST'])
def schedules():
   return render_template('nav_contents/schedules.html')

@views.route('/salaries', methods=['GET', 'POST'])
def salaries():
   return render_template('nav_contents/salaries.html')

@views.route('/announcements', methods=['GET', 'POST'])
def announcements():
   return render_template('nav_contents/announcements.html')
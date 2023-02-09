from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


schedules_bp = Blueprint('schedules_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@schedules_bp.route('/schedules', methods=['GET', 'POST'])
def schedules():
   return render_template('schedules.html')


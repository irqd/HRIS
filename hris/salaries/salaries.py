from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


salaries_bp = Blueprint('salaries_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@salaries_bp.route('/salaries', methods=['GET', 'POST'])
def salaries():
   return render_template('salaries.html')
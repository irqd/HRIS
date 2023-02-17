from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

profile_bp = Blueprint('profile_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')


@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
   return render_template('profile.html')
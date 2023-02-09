from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

home_bp = Blueprint('home_bp', __name__, template_folder='templates',
    static_folder='static', static_url_path='static')


@home_bp.route('/', methods=['GET', 'POST'])
@home_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
   return render_template('home.html')













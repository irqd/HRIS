from hris.models import *
from flask import Blueprint, render_template, request, flash, redirect, url_for


announcement_bp = Blueprint('announcement_bp', __name__,  template_folder='templates',
    static_folder='static', static_url_path='static')

@announcement_bp.route('/announcements', methods=['GET', 'POST'])
def announcements():
   return render_template('announcements.html')
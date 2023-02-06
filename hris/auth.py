from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import *
from flask_login import login_required, current_user, login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
@auth.route('login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
        return redirect(url_for('views.home'))
   if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      g = Users.query.filter_by(email=email).first()
      if g is not None:
            if g and g.verify_password(
                    attempted_password=password):
                  login_user(g)
                  print(current_user.email)
                  flash(f'Login Successful. You are now logged in as {g.email}',
                      category='success')
                  return redirect(url_for('views.home'))
            else:
               flash("Username and password didn't match, please try again", category='danger')
      else:
         flash(f'This user is not yet registered. Please Sign Up.', category='info')
      
   return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
   logout_user()
   return redirect(url_for('auth.login'))


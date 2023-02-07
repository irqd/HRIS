from hris.models import *
from hris.forms import *
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user


auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
@auth.route('login', methods=['GET', 'POST'])
def login():
   login_form = LoginForm()

   if current_user.is_authenticated:
        return redirect(url_for('views.home'))

   if login_form.validate_on_submit():
      attempted_user_email = Users.query.filter_by(email=login_form.email.data).first()

      if attempted_user_email is not None:
         if attempted_user_email and attempted_user_email.verify_password(
            attempted_password = login_form.password.data
         ):
            login_user(attempted_user_email)
            #print(login_form.access.data)
            flash(f'{attempted_user_email.email} logged in successfully.',
                     category='success')
            return redirect(url_for('views.home'))
         else:
            flash("Email and password didn't match. Please try again", category='danger')
      else:
         flash(f'This account is not registered in the system.', category='info')

   return render_template("login.html", login_form=login_form)


@auth.route('/logout')
@login_required
def logout():
   logout_user()
   flash(f'The user was logged out successful!y!', category='info')
   return redirect(url_for('auth.login'))


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from os import path
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()
DB_NAME = "hris"

def create_app():
   app = Flask(__name__)

   app.config['SECRET_KEY'] = 'fa282f581ec1d84bc02c6f34d4da17a2'

   #for sqlite
   #app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

   #for mysql
   app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:@localhost:3306/{DB_NAME}"
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
   db.init_app(app)

   #import blueprints
   from .announcements.announcement import announcement_bp
   from .attendance.attendance import attendance_bp
   from .auth.auth import auth_bp
   from .departments.departments import departments_bp
   from .employees.employees import employees_bp
   from .home.home import home_bp
   from .payroll.payroll import payroll_bp
   from .profile.profile import profile_bp
   from .schedules.schedules import schedules_bp
   from .salaries.salaries import salaries_bp
   
   #register Blueprints
   app.register_blueprint(home_bp, url_prefix='/')
   app.register_blueprint(auth_bp, url_prefix='/')
   app.register_blueprint(departments_bp, url_prefix='/')
   app.register_blueprint(employees_bp, url_prefix='/')
   app.register_blueprint(announcement_bp, url_prefix='/')
   app.register_blueprint(attendance_bp, url_prefix='/')
   app.register_blueprint(salaries_bp, url_prefix='/')
   app.register_blueprint(payroll_bp, url_prefix='/')
   app.register_blueprint(profile_bp, url_prefix='/')
   app.register_blueprint(schedules_bp, url_prefix='/')


   # from .models import Users, EmployeeInfo, Attendance, Leave, EmploymentInfo, Positions, Departments

   # for sqlite
   # if not path.exists('hris/instance' + DB_NAME):
   #    with app.app_context():
   #       db.create_all()
 
   # uncomment when creating new db.
   # with app.app_context():
   #    db.create_all()
 
   bcrypt.init_app(app)
   migrate.init_app(app, db)
   login_manager.login_view = 'auth_bp.login'
   login_manager.login_message_category = 'info'
   login_manager.init_app(app)
   
   return app

app = create_app()

# Custom error pages


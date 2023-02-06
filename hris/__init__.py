from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
DB_NAME = "hris"

def create_app():
   app = Flask(__name__)

   app.config['SECRET_KEY'] = 'fa282f581ec1d84bc02c6f34d4da17a2'
   #app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
   app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:@localhost:3306/{DB_NAME}"
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
   db.init_app(app)

   from .views import views
   from .auth import auth
   app.register_blueprint(auth, url_prefix='/')
   app.register_blueprint(views, url_prefix='/')


   from .models import Users, EmployeeInfo, Attendance, Leave, EmploymentInfo, Position, Department

   #for sqlite
   #if not path.exists('hris/instance' + DB_NAME):
   # with app.app_context():
   #    db.create_all()

   with app.app_context():
      db.create_all()
 
   bcrypt.init_app(app)
   login_manager.login_view = 'auth.login'
   login_manager.login_message_category = 'info'
   login_manager.init_app(app)
   
   return app
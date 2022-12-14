from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.modules.csrf import csrf
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg'


db =SQLAlchemy(app)
bcrypt=Bcrypt(app)
csrf.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application.routes import routes
from application.models import models
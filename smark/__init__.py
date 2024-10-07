from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from dotenv import load_dotenv
from .views import views

import os

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGO_URI'] = DATABASE_URI
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
db = PyMongo(app).db
bcrypt = Bcrypt(app)

app.register_blueprint(views, url_prefix='/')

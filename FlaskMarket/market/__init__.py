from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #config the app to recognize its db location
app.config['SECRET_KEY'] = '2c1ddf0cd19ab34f7bf1d59f' #CSRF TOKEN for the form
db = SQLAlchemy(app)  #creating a db instance
bcrypt = Bcrypt(app)  #producing hashes for passwords to be stored in db
from market import routes
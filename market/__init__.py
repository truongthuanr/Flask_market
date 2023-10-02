from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY' ] = "'3fbce8c32d13acdef267847d'"

db = SQLAlchemy(app)


from market import routes


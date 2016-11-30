import logging
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy


"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name='Flask Admin', template_mode='bootstrap3')
db = SQLAlchemy(app)

from app import views_register


__author__ = 'LeonSine'

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object("config")

# app.after_request(list)
# def list():
#     print 'receive request'

db = MongoEngine(app)

from app import views, model
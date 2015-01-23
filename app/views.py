__author__ = 'LeonSine'

from app import app
from flask import render_template
from app.model import Todo

@app.route('/')
def index():
    print 'coming in'
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route('/index')
def init():
    return render_template("index.html", todos="This")

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
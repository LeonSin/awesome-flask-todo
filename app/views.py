__author__ = 'LeonSine'

from app import app
from flask import render_template, request
from app.model import Todo

@app.route('/')
def index():
    print 'coming in'
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST', ])
def add():
    content = request.form.get("content")
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@app.route('/index')
def init():
    return render_template("index.html", todos="This")

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
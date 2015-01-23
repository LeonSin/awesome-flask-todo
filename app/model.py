#


from app import db
import datetime

class Todo(db.Document):
    content = db.StringField(required=True, max_length=20) # the content of to-do
    time = db.DateTimeField(default=datetime.datetime.now()) # the release time of to-do
    status = db.IntField(default=0) # state of complete of to-do


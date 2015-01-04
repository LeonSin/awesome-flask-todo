__author__ = 'LeonSine'

# import Class Flask to create application
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# create index method
# use decorator to bound the route rules
@app.route("/")
def index():
    return "Hello World"

# Run!
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
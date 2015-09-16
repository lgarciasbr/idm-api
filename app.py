__author__ = 'leandro'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

app.run()
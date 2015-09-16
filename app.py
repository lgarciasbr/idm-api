__author__ = 'leandro'

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!", 200

app.run()
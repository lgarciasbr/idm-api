from flask import Flask
from Account.controller import account_blueprint
from Authentication.controller import authentication_blueprint
from Home.controller import home_blueprint
from Errors.controller import error_blueprint
import gunicorn

app = Flask(__name__)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(error_blueprint)

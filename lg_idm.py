from flask import Flask, request, jsonify
from Account.controller import account_blueprint
from Authentication.controller import authentication_blueprint
from Home.controller import home_blueprint
from config import MSN_400, MSN_404, MSN_405
import gunicorn

app = Flask(__name__)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(home_blueprint)


# todo separar os erros em um modulo so para cuidar disso.
# Error
@app.errorhandler(400)
def bad_request(error):
    message = {
        'status': 400,
        'message': MSN_400 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': MSN_404 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(405)
def not_allowed(error):
    message = {
        'status': 405,
        'message': MSN_405 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 405

    return resp

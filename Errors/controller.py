from flask import Blueprint, request, jsonify
from config import MSN_404

error_blueprint = Blueprint('errors', __name__)


@error_blueprint.app_errorhandler(404)
def not_found(error):
    message = {
        'status': 405,
        'message': MSN_404 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

'''
from httplib import HTTPException
from flask import jsonify, request, current_app
from werkzeug.exceptions import default_exceptions


def error_handler(error):
    msg = "Request resulted in {}".format(error)
    current_app.logger.warning(msg, exc_info=error)

    if isinstance(error, HTTPException):
        description = error.get_description(request.environ)
        code = error.code
        name = error.name + ' ' + request.url
    else:
        description = ("We encountered an error "
                       "while trying to fulfill your request")
        code = 500
        name = 'Internal Server Error'

    message = {
        'status': code,
        'message': name + ' ' + request.url
    }

    resp = jsonify(message)
    resp.status_code = code

    return resp


def init_app(app):
    for exception in default_exceptions:
        app.register_error_handler(exception, error_handler)

    app.register_error_handler(Exception, error_handler)
'''

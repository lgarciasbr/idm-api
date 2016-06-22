from flask import Blueprint

account_blueprint = Blueprint('accounts', __name__)


@account_blueprint.before_request
def before_request():
    pass


@account_blueprint.after_request
def after_request(rv):
    return rv


from . import error_handler_controller, home_controller, account_controller

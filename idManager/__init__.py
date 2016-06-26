from flask import Blueprint

id_manager_blueprint = Blueprint('accounts', __name__)


@id_manager_blueprint.before_request
def before_request():
    pass


@id_manager_blueprint.after_request
def after_request(rv):
    return rv


from . import error_handler_controller, home_controller, account_controller, authentication_controller

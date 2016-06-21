from flask import Blueprint

account_blueprint = Blueprint('accounts', __name__)


@account_blueprint.before_request
def before_request():
    """All routes in this blueprint require authentication."""
    pass


@account_blueprint.after_request
def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv


from . import error_handler_controller

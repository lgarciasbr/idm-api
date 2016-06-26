from idManager.view import error_handler_view
from . import id_manager_blueprint


@id_manager_blueprint.app_errorhandler(404)
def not_found(e):
    response = error_handler_view.not_found(e)

    return response


@id_manager_blueprint.errorhandler(403)
def forbidden(e):
    response = error_handler_view.forbidden(e)

    return response


@id_manager_blueprint.errorhandler(400)
def bad_request(e):
    response = error_handler_view.bad_request(e)

    return response
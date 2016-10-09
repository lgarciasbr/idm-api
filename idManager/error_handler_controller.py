import idManager.view.header_view
from idManager.view import error_handler_view
from . import id_manager_blueprint


@id_manager_blueprint.app_errorhandler(500)
@idManager.view.header_view.add_response_headers
def not_allowed(e):
    response = error_handler_view.internal_server_error(e)
    response.status_code = 500

    return response


@id_manager_blueprint.app_errorhandler(405)
#@idManager.view.header_view.add_response_headers
def not_allowed(e):
    response = error_handler_view.not_allowed(e)
    response.status_code = 405

    return response


@id_manager_blueprint.app_errorhandler(404)
@idManager.view.header_view.add_response_headers
def not_found(e):
    response = error_handler_view.not_found(e)
    response.status_code = 404

    return response


@id_manager_blueprint.errorhandler(403)
@idManager.view.header_view.add_response_headers
def forbidden(e):
    response = error_handler_view.forbidden(e)
    response.status_code = 403

    return response


# Bad Request don' call the decorator add_response_headers, because it is a bad_request. ;-)
@id_manager_blueprint.errorhandler(400)
def bad_request(e):
    response = error_handler_view.bad_request(e)
    response.status_code = 400

    return response

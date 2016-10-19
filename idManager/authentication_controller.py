from flask import request, abort, current_app
import idManager.view.header_view
from idManager.model import authentication_service, account_service
from idManager.view import authentication_view
from . import id_manager_blueprint
from idManager.settings import MSN_EXPECTED_JSON_DATA


# todo 2 steps verification - http://blog.miguelgrinberg.com/post/two-factor-authentication-with-flask

@id_manager_blueprint.route('/auth/', methods=['POST'])
@idManager.view.header_view.add_response_headers
def auth_login():
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        current_app.extensions['sentry'].captureMessage('auth_login, 400: ' + MSN_EXPECTED_JSON_DATA)
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account_data, errors = account_service.register_account_schema.load(data)
    if errors:
        current_app.extensions['sentry'].captureMessage('auth_login, 400: ' + str(errors))
        abort(400, errors)

    auth = authentication_service.auth_login(ver, account_data)
    return authentication_view.auth_login(auth), auth.get('http_status_code')


@id_manager_blueprint.route('/auth/', methods=['GET'])
@idManager.view.header_view.add_response_headers
def auth_is_valid():
    ver = request.headers.get('ver')
    token = request.headers.get('token')

    auth = authentication_service.auth_is_valid(ver, token)
    return authentication_view.auth_is_valid(auth), auth.get('http_status_code')


@id_manager_blueprint.route('/auth/', methods=['DELETE'])
@idManager.view.header_view.add_response_headers
def auth_logout():
    ver = request.headers.get('ver')
    token = request.headers.get('token')

    auth = authentication_service.auth_logout(ver, token)
    return authentication_view.auth_logout(auth), auth.get('http_status_code')

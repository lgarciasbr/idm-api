from flask import request
from idManager.model import authentication_service, token_service, account_service, message_service
from idManager.view import authentication_view, header_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/auth/', methods=['POST'])
@header_view.verify_content_type
@header_view.add_response_headers
def auth_login():
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        # Bad Request
        message_service.expected_json_data()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        # Validate Schema using the write version.
        account_data, errors = account_service.register_account_schema.load(data)
        if errors:
            # Bad Request
            message_service.wrong_json_data(errors)

        auth = authentication_service.auth_login_ver_1(account_data["email"], account_data["password"])

        response = authentication_view.auth_login(**auth)
        response.status_code = auth.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return auth_login_ver_2(username, password, ip)
    else:
        # Bad Request
        message_service.invalid_api_ver()


@id_manager_blueprint.route('/auth/', methods=['GET'])
@header_view.verify_content_type
@token_service.validate_token
@header_view.add_response_headers
def auth_is_valid():
    ver = request.headers.get('ver')
    token = request.headers.get('token')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        auth = authentication_service.auth_is_valid_ver_1(token)

        response = authentication_view.auth_is_valid(**auth)
        response.status_code = auth.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return auth_logout_ver_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()


@id_manager_blueprint.route('/auth/', methods=['DELETE'])
@header_view.verify_content_type
@token_service.validate_token
@header_view.add_response_headers
def auth_logout():
    ver = request.headers.get('ver')
    token = request.headers.get('token')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        auth = authentication_service.auth_logout_ver_1(token)

        response = authentication_view.auth_logout(**auth)
        response.status_code = auth.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return auth_is_valid_ver_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()

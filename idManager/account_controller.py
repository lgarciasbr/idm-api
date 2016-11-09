from flask import request
import idManager.view.header_view
from idManager.model import account_service, token_service, message_service
from idManager.view import account_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/accounts/', methods=['POST'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def register_account():
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        # Bad Request
        message_service.message_expected_json_data()

    # Use 'or not ver' at the last version
    if ver == '1' or not ver:
        # Validate Schema using the write version.
        account_data, errors = account_service.register_account_schema.load(data)
        if errors:
            # Bad Request
            message_service.message_wrong_json_data(errors)

        account_data = account_service.account_register_ver_1(account_data["email"], account_data["password"])

        response = account_view.register_account(**account_data)
        response.status_code = account_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return account_service.account_register_ver_2()
    else:
        # Bad Request
        message_service.message_invalid_api_ver()


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['PUT'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
def change_account_password(pk):
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        # Bad Request
        message_service.message_expected_json_data()

    if not pk:
        # Bad Request
        message_service.message_expected_id()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        # Validate Schema using the write version.
        account_password, errors = account_service.change_account_password_schema.load(data)
        if errors:
            # Bad Request
            message_service.message_wrong_json_data(errors)

        account_data = account_service.change_account_password_ver_1(pk, account_password['password'],
                                                                     account_password['new_password'])

        response = account_view.account_change_password(**account_data)
        response.status_code = account_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return account_service.change_account_password_ver_2()
    else:
        # Bad Request
        message_service.message_invalid_api_ver()


@id_manager_blueprint.route('/accounts/', methods=['GET'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
def get_accounts():
    ver = request.headers.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        accounts_data = account_service.get_accounts_ver_1()

        response = account_view.get_accounts(**accounts_data)
        response.status_code = accounts_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return get_accounts_ver_2()
    else:
        # Bad Request
        message_service.message_invalid_api_ver()


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['GET'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
def get_account_by_id(pk):
    ver = request.headers.get('ver')

    if not pk:
        # Bad Request
        message_service. message_expected_id()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        account_data = account_service.get_account_by_id_ver_1(pk)

        response = account_view.get_account_by_id(**account_data)
        response.status_code = account_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return get_account_by_id_2()
    else:
        # Bad Request
        message_service.message_invalid_api_ver()


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['DELETE'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
def delete_account_by_id(pk):
    ver = request.headers.get('ver')

    if not pk:
        # Bad Request
        message_service.message_expected_id()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        account_data = account_service.delete_account_by_id_ver_1(pk)

        response = account_view.delete_account(**account_data)
        response.status_code = account_data.get('http_status_code')
    # elif header['ver'] == '2':
    #    return delete_account_by_id_ver_2()
    else:
        # Bad Request
        message_service.message_invalid_api_ver()

    return response

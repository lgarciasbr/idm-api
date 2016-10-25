from flask import request, abort
import idManager.view.header_view
from idManager.model import account_service
from idManager.model import message_service
from idManager.settings import MSN_EXPECTED_JSON_DATA
from idManager.view import account_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/accounts/', methods=['POST'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def register_account():
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        message_service.send_log_message('account_register, 400: ' + MSN_EXPECTED_JSON_DATA)
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account_data, errors = account_service.register_account_schema.load(data)
    if errors:
        message_service.send_log_message('account_register, 400: ' + str(errors))
        abort(400, errors)

    account_data = account_service.account_register(ver, account_data)

    response = account_view.register_account(**account_data)
    response.status_code = account_data.get('http_status_code')

    return response


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['PUT'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def change_account_password(pk):
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data or not pk:
        message_service.send_log_message('change_account_password, 400: ' + MSN_EXPECTED_JSON_DATA)
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account_password, errors = account_service.change_account_password_schema.load(data)
    if errors:
        message_service.send_log_message('change_account_password, 400: ' + errors)
        abort(400, errors)

    account_data = account_service.change_account_password(ver, account_password, pk)

    response = account_view.account_change_password(**account_data)
    response.status_code = account_data.get('http_status_code')

    return response


@id_manager_blueprint.route('/accounts/', methods=['GET'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def get_accounts():
    ver = request.headers.get('ver')
    accounts_data = account_service.get_accounts(ver)

    response = account_view.get_accounts(**accounts_data)
    response.status_code = accounts_data.get('http_status_code')

    return response


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['GET'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def get_account_by_id(pk):
    ver = request.headers.get('ver')
    account_data = account_service.get_account_by_id(ver, pk)

    response = account_view.get_account_by_id(**account_data)
    response.status_code = account_data.get('http_status_code')

    return response


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['DELETE'])
@idManager.view.header_view.verify_content_type
@idManager.view.header_view.add_response_headers
def delete_account_by_id(pk):
    ver = request.headers.get('ver')
    account_data = account_service.delete_account_by_id(ver, pk)

    response = account_view.delete_account(**account_data)
    response.status_code = account_data.get('http_status_code')

    return response

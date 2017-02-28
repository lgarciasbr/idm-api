from flask import request
import idManager.view.header_view
from idManager.model import group_service, token_service, message_service
from idManager.view import group_view
from . import id_manager_blueprint
from idManager.settings import MAX_PER_PAGE
from flask_cors import cross_origin


@id_manager_blueprint.route('/groups/', methods=['POST'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
@cross_origin()
def register_group():
    ver = request.headers.get('ver')
    data = request.get_json(force=True, silent=True)

    if not data:
        # Bad Request
        message_service.expected_json_data()

    # Use 'or not ver' at the last version
    if ver == '1' or not ver:
        # Validate Schema using the write version.
        group_data, errors = group_service.group_schema.load(data)
        if errors:
            # Bad Request
            message_service.wrong_json_data(errors)

        group_data = group_service.group_register_ver_1(group_data["name"])

        response = group_view.register_group(**group_data)
        response.status_code = group_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return account_service.account_register_ver_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()


@id_manager_blueprint.route('/groups/', methods=['GET'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
@cross_origin()
def get_groups():
    ver = request.headers.get('ver')

    # Use 'or not ver' at the last version
    if ver == '1' or not ver:
        page = max(request.args.get('page', 1, type=int), 1)
        per_page = max(min(request.args.get('per_page', MAX_PER_PAGE,
                                            type=int), MAX_PER_PAGE),
                       1)

        groups_data = group_service.get_groups_ver_1(page, per_page)

        response = group_view.get_groups(**groups_data)
        response.status_code = groups_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return get_accounts_ver_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()


@id_manager_blueprint.route('/groups/<int:pk>', methods=['GET'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
@cross_origin()
def get_group_by_id(pk):
    ver = request.headers.get('ver')

    if not pk:
        # Bad Request
        message_service. expected_id()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        group_data = group_service.get_group_by_id_ver_1(pk)

        response = group_view.get_group_by_id(**group_data)
        response.status_code = group_data.get('http_status_code')

        return response
    # elif header['ver'] == '2':
    #    return get_account_by_id_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()


@id_manager_blueprint.route('/groups/<int:pk>', methods=['DELETE'])
@idManager.view.header_view.verify_content_type
@token_service.validate_token
@idManager.view.header_view.add_response_headers
@cross_origin()
def delete_group_by_id(pk):
    ver = request.headers.get('ver')

    if not pk:
        # Bad Request
        message_service.expected_id()

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        group_data = group_service.delete_group_by_id_ver_1(pk)

        response = group_view.delete_group(**group_data)
        response.status_code = group_data.get('http_status_code')
    # elif header['ver'] == '2':
    #    return delete_account_by_id_ver_2()
    else:
        # Bad Request
        message_service.invalid_api_ver()

    return response

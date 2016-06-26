from idManager.model.service import authentication_service
from idManager import authentication_view
from . import id_manager_blueprint
from flask import request


# todo 2 steps verification - http://blog.miguelgrinberg.com/post/two-factor-authentication-with-flask

@id_manager_blueprint.route('/auth/', methods=['POST'])
def auth_login():
    response = authentication_service.login(request.headers, request.json)
    http_status_code = response.get('http_status_code')

    return authentication_view.message_json(response), http_status_code


@id_manager_blueprint.route('/auth/', methods=['GET'])
def auth_is_valid():
    response = authentication_service.is_token_valid(request.headers)
    http_status_code = response.get('http_status_code')

    return authentication_view.message_json(response), http_status_code


@id_manager_blueprint.route('/auth/', methods=['DELETE'])
def auth_logout():
    response = authentication_service.logout(request.headers)
    http_status_code = response.get('http_status_code')

    return authentication_view.message_json(response), http_status_code

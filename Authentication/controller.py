from Authentication import view
from flask import request, Blueprint
from Authentication.model.service import authentication_service

authentication_blueprint = Blueprint('authentication', __name__)


# todo 2 steps verification - http://blog.miguelgrinberg.com/post/two-factor-authentication-with-flask

@authentication_blueprint.route('/auth/', methods=['POST'])
def auth_login():
    response = authentication_service.login(request.headers, request.json)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status


@authentication_blueprint.route('/auth/', methods=['GET'])
def auth_is_valid():
    response = authentication_service.is_token_valid(request.headers)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status


@authentication_blueprint.route('/auth/', methods=['DELETE'])
def auth_logout():
    response = authentication_service.logout(request.headers)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status

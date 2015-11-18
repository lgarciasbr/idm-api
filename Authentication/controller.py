from Authentication import view
from flask import request, Blueprint
from Authentication.model.service import authentication_service

authentication_blueprint = Blueprint('authentication', __name__)


@authentication_blueprint.route('/auth', methods=['POST'])
def auth_login():
    response = authentication_service.login(request.headers, request.json)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status


@authentication_blueprint.route('/auth', methods=['DELETE'])
def auth_logout():
    response = authentication_service.logout(request.headers)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status

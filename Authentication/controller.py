from Authentication import view
from flask import request, Blueprint
from Authentication.model.service import login_service, logout_service

authentication_blueprint = Blueprint('authentication', __name__)


@authentication_blueprint.route('/login', methods=['POST'])
def login():
    response = login_service.login(request.headers, request.json)
    http_code_status = response.get('http_code_status')
    return view.message_json(response), http_code_status


@authentication_blueprint.route('/logout', methods=['POST'])
def logout():
    response = logout_service.logout(request.headers)
    http_code_status = response.get('http_code_status')
    return view.message_json(response), http_code_status
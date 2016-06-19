from flask import request, Blueprint
from Account import view
from Account.model.service import account_service

account_blueprint = Blueprint('accounts', __name__)


def account_get_email(email):
    return account_service.get_user_by_email(email)


@account_blueprint.route('/accounts/', methods=['POST'])
def account_register():
    response = account_service.register(request.headers, request.json)
    http_code_status = response.get('http_code_status')
    message = response.get('message')
    return view.account_register(message), http_code_status


@account_blueprint.route('/accounts/', methods=['GET'])
def account_get():
    response = account_service.get(request.headers)
    http_code_status = response.get('http_code_status')
    message = response.get('message')
    return view.account_get(message), http_code_status

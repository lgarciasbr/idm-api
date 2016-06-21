from flask import request, Blueprint
from Account import view
from Account.model.service import account_service
from flask import jsonify

account_blueprint = Blueprint('accounts', __name__)


def account_get_email(email):
    return account_service.get_user_by_email(email)


@account_blueprint.route('/accounts/', methods=['POST'])
def account_register():
    response = account_service.register(request.headers, request.json)
    return view.account_register(response)


@account_blueprint.route('/accounts/', methods=['GET'])
def accounts_get():
    response = account_service.accounts_get(request.headers)
    return view.accounts_get(response)


@account_blueprint.route('/accounts/<int:pk>', methods=['GET'])
def account_get(pk):
    response = account_service.account_get(request.headers, pk)
    return view.account_get(response)


@account_blueprint.app_errorhandler(404)  # this has to be an app-wide handler
def not_found(e):
    response = jsonify({'status': 404, 'error': 'not found',
                        'message': 'invalid resource URI'})
    response.status_code = 404
    return response


@account_blueprint.errorhandler(400)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': e.description})
    response.status_code = 400
    return response
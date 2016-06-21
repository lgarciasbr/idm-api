from flask import request
from . import account_blueprint
from Account import account_view
from Account.model.service import account_service


def account_get_email(email):
    return account_service.get_user_by_email(email)


@account_blueprint.route('/accounts/', methods=['POST'])
def account_register():
    account = account_service.register(request.headers, request.json)
    return account_view.account_register(account)


@account_blueprint.route('/accounts/', methods=['GET'])
def accounts_get():
    accounts = account_service.accounts_get(request.headers)
    return account_view.accounts_get(accounts)


@account_blueprint.route('/accounts/<int:pk>', methods=['GET'])
def account_get(pk):
    account = account_service.account_get(request.headers, pk)
    return account_view.account_get(account)

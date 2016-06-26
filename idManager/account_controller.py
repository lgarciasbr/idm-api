from flask import request
from idManager.model.service import account_service
from idManager.view import account_view
from . import id_manager_blueprint


def account_get_email(email):
    return account_service.get_account_by_email(email)


@id_manager_blueprint.route('/accounts/', methods=['POST'])
def account_register():
    account = account_service.account_register(request.headers, request.get_json(force=True, silent=True))
    return account_view.account_register(account)


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['PUT'])
def account_change_password(pk):
    account = account_service.account_change_password(request.headers, request.get_json(force=True, silent=True), pk)
    return account_view.account_register(account)


@id_manager_blueprint.route('/accounts/', methods=['GET'])
def accounts_get():
    accounts = account_service.accounts_get(request.headers)
    return account_view.accounts_get(accounts)


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['GET'])
def account_get(pk):
    account = account_service.account_get(request.headers, pk)
    return account_view.account_get(account)


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['DELETE'])
def account_delete(pk):
    account = account_service.account_delete(request.headers, pk)
    return account_view.account_delete(account)

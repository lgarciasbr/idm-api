from flask import request
from idManager.model.service import account_service
from idManager.view import account_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/accounts/', methods=['POST'])
def register_account():
    account = account_service.account_register(request.headers, request.get_json(force=True, silent=True))
    return account_view.register_account(account), account.get('http_status_code')


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['PUT'])
def change_account_password(pk):
    account = account_service.account_change_password(request.headers, request.get_json(force=True, silent=True), pk)
    return account_view.account_change_password(account), account.get('http_status_code')


@id_manager_blueprint.route('/accounts/', methods=['GET'])
def get_accounts():
    accounts = account_service.get_accounts(request.headers)
    return account_view.get_accounts(accounts), accounts.get('http_status_code')


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['GET'])
def get_account_by_id(pk):
    account = account_service.get_account_by_id(request.headers, pk)
    return account_view.get_account_by_id(account), account.get('http_status_code')


@id_manager_blueprint.route('/accounts/<int:pk>', methods=['DELETE'])
def delete_account_by_id(pk):
    account = account_service.delete_account_by_id(request.headers, pk)
    return account_view.delete_account(account), account.get('http_status_code')

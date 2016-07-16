from flask import jsonify


def register_account(account):
    http_status_code = account.get('http_status_code')
    message = account.get('message')
    account_created = account.get('account')
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account_created.data})

    return view


def get_accounts(accounts):
    http_status_code = accounts.get('http_status_code')
    accounts = accounts.get('accounts')
    view = jsonify({'status_code': http_status_code, 'accounts': accounts.data})

    return view


def get_account_by_id(account):
    http_status_code = account.get('http_status_code')
    account = account.get('account')
    view = jsonify({'status_code': http_status_code, 'account': account.data})

    return view


def delete_account(account):
    http_status_code = account.get('http_status_code')
    message = account.get('message')
    account_deleted = account.get('account')
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account_deleted.data})

    return view

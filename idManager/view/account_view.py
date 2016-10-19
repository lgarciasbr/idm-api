from flask import jsonify


def register_account(http_status_code, account, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account.data})

    return view


def account_change_password(http_status_code, account, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account.data})

    return view


def get_accounts(http_status_code, accounts):
    view = jsonify({'status_code': http_status_code, 'accounts': accounts.data})

    return view


def get_account_by_id(http_status_code, account):
    view = jsonify({'status_code': http_status_code, 'account': account.data})

    return view


def delete_account(http_status_code, account, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account.data})

    return view

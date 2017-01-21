from flask import jsonify


def register_account(http_status_code, account, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account.data})

    return view


def account_change_password(http_status_code, message):
    view = jsonify({'status_code': http_status_code, 'message': message})

    return view


def get_accounts(accounts, total, pages, http_status_code):

    view = jsonify({'accounts': accounts.data,
                    'total': total,
                    'pages': pages,
                    'status_code': http_status_code})

    return view


def get_account_by_id(http_status_code, account):
    view = jsonify({'status_code': http_status_code, 'account': account.data})

    return view


def delete_account(http_status_code, account, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'account': account.data})

    return view

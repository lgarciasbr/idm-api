from flask import jsonify


# todo implementar o retorno com xml
def account_register(account):
    http_status_code = account.get('http_status_code')
    message = account.get('message')
    
    response = jsonify({'status': http_status_code, 'message': message})
    response.status_code = http_status_code

    return response


def accounts_get(accounts):
    http_status_code = accounts.get('http_status_code')
    message = accounts.get('message')

    response = jsonify({'status': http_status_code, 'accounts': message.data})
    response.status_code = http_status_code

    return response


def account_get(account):
    http_status_code = account.get('http_status_code')
    message = account.get('message')

    response = jsonify({'status': http_status_code, 'account': message.data})

    response.status_code = http_status_code

    return response
from flask import jsonify


# todo implementar o retorno com xml
def account_register(response):
    http_code_status = response.get('http_code_status')
    message = response.get('message')

    return jsonify({'status': http_code_status,
                    'message': message}), \
           http_code_status


def accounts_get(response):
    http_code_status = response.get('http_code_status')
    message = response.get('message')

    return jsonify({'status': http_code_status,
                    'accounts': message.data}), \
           http_code_status


def account_get(response):
    http_code_status = response.get('http_code_status')
    message = response.get('message')

    return jsonify({'status': http_code_status,
                    'account': message.data}), \
           http_code_status

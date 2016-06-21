from flask import jsonify


# todo implementar o retorno com xml
def account_register(response):
    http_status_code = response.get('http_status_code')
    message = response.get('message')
    
    response = jsonify({'status': http_status_code, 'message': message})
    response.status_code = http_status_code

    return response


def accounts_get(response):
    http_status_code = response.get('http_status_code')
    message = response.get('message')

    return jsonify({'status': http_status_code,
                    'accounts': message.data}), \
           http_status_code


def account_get(response):
    http_status_code = response.get('http_status_code')
    message = response.get('message')

    return jsonify({'status': http_status_code,
                    'account': message.data}), \
           http_status_code

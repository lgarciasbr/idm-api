from flask import jsonify


def auth_login(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    auth = auth.get('auth')

    response = jsonify({'status_code': http_status_code, 'message': message, 'auth': auth})
    response.status_code = http_status_code

    return response


def auth_is_valid(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    token = auth.get('token')

    response = jsonify({'status_code': http_status_code, 'message': message, 'auth': {'_token': token}})
    response.status_code = http_status_code

    return response


def auth_logout(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    token = auth.get('token')

    response = jsonify({'status_code': http_status_code, 'message': message, 'auth': {'_token': token}})
    response.status_code = http_status_code

    return response
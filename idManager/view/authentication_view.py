from flask import jsonify


def auth_login(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    token = auth.get('token')

    view = jsonify({'status_code': http_status_code, 'message': message, 'auth': {'_token': token}})

    return view


def auth_is_valid(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    token = auth.get('token')

    view = jsonify({'status_code': http_status_code, 'message': message, 'auth': {'_token': token}})

    return view


def auth_logout(auth):
    http_status_code = auth.get('http_status_code')
    message = auth.get('message')
    token = auth.get('token')

    view = jsonify({'status_code': http_status_code, 'message': message, 'auth': {'_token': token}})

    return view

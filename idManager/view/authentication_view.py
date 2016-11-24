from flask import jsonify


def auth_login(http_status_code, message, token):
    view = jsonify({'status_code': http_status_code, 'message': message, '_token': token})

    return view


def auth_is_valid(http_status_code, message, token):
    view = jsonify({'status_code': http_status_code, 'message': message, '_token': token})

    return view


def auth_logout(http_status_code, message, token):
    view = jsonify({'status_code': http_status_code, 'message': message, '_token': token})

    return view

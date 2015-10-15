import traceback

from flask import jsonify

from Account.model.service.login import login_v1
from Account.model.service.logout import logout_v1
from config import MSN_400


def login_controller(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return login_v1(data['username'], data['password'])
    except ValueError:
        traceback.print_exception()

    return jsonify({'message': MSN_400}), 400


def logout_controller(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return logout_v1(header['token'])
    except ValueError:
        traceback.print_exception()

    return jsonify({'message': MSN_400}), 400

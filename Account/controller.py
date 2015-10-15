import traceback

from flask import jsonify

from Account.model.service import login
from Account.model.service.logout import logout_v1
from config import MSN_400


def login_controller(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return login.ver_1(data['username'], data['password'])
            # elif header['ver'] == '2':
            #    return login.ver_1(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    return jsonify({'message': MSN_400}), 400


def logout_controller(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return logout_v1(header['token'])
    except Exception:
        pass

    return jsonify({'message': MSN_400}), 400

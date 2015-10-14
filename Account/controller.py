from flask import jsonify
from Account.service.login import login_v1
from config import MSN_400

import traceback


def login_controller(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return login_v1(data['username'], data['password'])
    except ValueError:
        traceback.print_exception()

    return jsonify({'message': MSN_400}), 400

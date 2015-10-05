from flask import jsonify
from Account.service.token import set_token
from config import MSG_LOGIN


def login_v1(username, password):

    # todo implementar a chamada via banco de dados
    if username == 'admin' and password == 'default':

        token = set_token({'username': username})

        return jsonify({'message': MSG_LOGIN, 'token': token}), 200
    else:
        raise Exception()

from flask import jsonify

from Account.model.service.token import set_token
from config import MSG_LOGIN, MSG_LOGIN_ERROR


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def ver_1(username, password):

    # todo implementar a chamada via banco de dados
    if username == 'admin' and password == 'default':
        token = set_token({'username': username})

        return jsonify({'message': MSG_LOGIN, 'token': token}), 200

    else:
        return jsonify({'message': MSG_LOGIN_ERROR}), 403

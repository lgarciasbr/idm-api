from flask import jsonify

from Account.model.service.token_service import set_token
from config import MSG_LOGIN, MSG_LOGIN_ERROR, MSN_400


def login(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return ver_1(data['username'], data['password'])
            # elif header['ver'] == '2':
            #    return login.ver_1(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    return jsonify({'message': MSN_400}), 400


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def ver_1(username, password):

    # todo implementar a chamada via banco de dados
    if username == 'admin' and password == 'default':
        token = set_token({'username': username})

        return jsonify({'message': MSG_LOGIN, 'token': token}), 200

    else:
        return jsonify({'message': MSG_LOGIN_ERROR}), 403

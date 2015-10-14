from flask import jsonify
from Account.service.token import set_token
from config import MSG_LOGIN, MSG_LOGIN_ERROR


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def login(header, body):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == 1:
                return login_v1(body['username'], body['password'])
            else:
                # Always use last version here.
                return login_v1(body['username'], body['password'])
        else:
            pass
    except:
        pass

    return jsonify({'message': MSG_LOGIN_ERROR}), 403


def login_v1(username, password):

    # todo implementar a chamada via banco de dados
    if username == 'admin' and password == 'default':
        token = set_token({'username': username})

        return jsonify({'message': MSG_LOGIN, 'token': token}), 200
    else:
        raise Exception()

from flask import jsonify

from Account.model.service.token_service import get_token, delete_token
from config import MSG_LOGOUT, MSG_INVALID_TOKEN, MSN_400


def logout(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return logout_ver_1(header['token'])
            # elif header['ver'] == '2':
            #    return logout_ver_1(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    return jsonify({'message': MSN_400}), 400


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def logout_ver_1(token):
    user = get_token(token)

    if user is not None:
        delete_token(token)
        return jsonify({'message': MSG_LOGOUT}), 200
    else:
        return jsonify({'message': MSG_INVALID_TOKEN, 'token': token}), 403


def logout_ver_2(token, ip):
    pass

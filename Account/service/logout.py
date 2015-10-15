from flask import jsonify
from Account.service.token import get_token, delete_token
from config import MSG_LOGOUT, MSG_INVALID_TOKEN


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def logout_v1(token):
    user = get_token(token)

    if user is not None:
        delete_token(token)
        return jsonify({'message': MSG_LOGOUT}), 200
    else:
        return jsonify({'message': MSG_INVALID_TOKEN, 'token': token}), 403

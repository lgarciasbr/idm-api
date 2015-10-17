from Account.model.service.token_service import set_token
from config import MSG_LOGIN, MSG_LOGIN_ERROR, MSN_400


def login(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return login_ver_1(data['username'], data['password'])
            # elif header['ver'] == '2':
            #    return login_ver_2(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


# todo precisa funcionar mesmo sem a versao
# todo implementar unittest aqui no login ???
def login_ver_1(username, password):

    # todo implementar a chamada via banco de dados
    if username == 'admin' and password == 'default':
        token = set_token({'username': username})
        # Login
        return {'message': MSG_LOGIN, 'token': token, 'http_code_status': 200}

    else:
        # Forbidden
        return {'message': MSG_LOGIN_ERROR, 'http_code_status': 403}


def login_ver_2(username, password, ip):
    pass

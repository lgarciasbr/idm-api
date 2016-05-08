import bcrypt
from Account import controller
from Authentication.model.service import token_service
from Authentication.model.service.token_service import get_token, delete_token
from settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSN_400, MSG_LOGOUT, MSG_INVALID_TOKEN, MSG_VALID_TOKEN


# todo Implementar o timeout do login, precisa pensar nas regras.
def login(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return login_ver_1(data['email'], data['password'])
            # elif header['ver'] == '2':
            #    return login_ver_2(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


def login_ver_1(email, password):

    user = controller.account_get_email(email)

    if user is not None and user.password == bcrypt.hashpw(password.encode('utf-8'), user.password):
        token = token_service.set_token(user)
        # Allowed
        return {'message': MSG_LOGIN, 'token': token, 'http_code_status': 200}

    else:
        # Forbidden
        return {'message': MSG_LOGIN_ERROR, 'http_code_status': 403}


def login_ver_2(username, password, ip):
    pass


def logout(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return logout_ver_1(header['token'])
            # elif header['ver'] == '2':
            #    return logout_ver_1(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


def logout_ver_1(token):
    user = get_token(token)

    if user is not None:
        delete_token(token)
        # Logout
        return {'message': MSG_LOGOUT, 'token': token, 'http_code_status': 200}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_code_status': 403}


def logout_ver_2(token, ip):
    pass


# todo Criar test para o is_valid_token
# todo Com o timeout do login implementado o is_valid_token pode fazer um refresh no timeout.
def is_token_valid(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return is_token_valid_ver_1(header['token'])
            # elif header['ver'] == '2':
            #    return is_token_valid_ver_1(data['username'], data['password'], data['ip'])
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


def is_token_valid_ver_1(token):
    user = get_token(token)

    if user is not None:
        # Allowed
        return {'message': MSG_VALID_TOKEN, 'http_code_status': 200}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_code_status': 403}

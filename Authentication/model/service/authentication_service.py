import bcrypt
from Account import controller
from Authentication.model.service import token_service
from Authentication.model.service.token_service import get_token, delete_token
from settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSN_400, MSG_LOGOUT, MSG_INVALID_TOKEN, MSG_VALID_TOKEN, SECRET_KEY
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

# region Token


# todo Implementar o timeout do login, precisa pensar nas regras.
def generate_auth_token(user, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return (s.dumps(user.id)).decode('ascii')


def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    try:
        user_id = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    user_id_registered_token = get_token(token)

    if user_id_registered_token is None or user_id_registered_token != user_id:
        return None  # valid token, but different user

    return user_id

# endregion

# region LOGIN


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
        token = token_service.set_token(generate_auth_token(user), user)
        # Allowed
        return {'message': MSG_LOGIN, 'token': token, 'http_code_status': 200}

    else:
        # Forbidden
        return {'message': MSG_LOGIN_ERROR, 'http_code_status': 403}


def login_ver_2(username, password, ip):
    pass

# endregion

# region LOGOUT


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
    user_id = verify_auth_token(token)

    if user_id is not None:
        delete_token(token)
        # Logout
        return {'message': MSG_LOGOUT, 'token': token, 'http_code_status': 200}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_code_status': 403}


def logout_ver_2(token, ip):
    pass

# endregion

# region Is token valid?


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
    user_id = verify_auth_token(token)

    if user_id is not None:
        # Allowed
        return {'message': MSG_VALID_TOKEN, 'http_code_status': 200}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_code_status': 403}

# endregion

import bcrypt
from Account import controller
from Authentication.model.service import token_service
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


def login_ver_1(email, password):

    user = controller.account_get_email(email)

    if user is not None and user.password == bcrypt.hashpw(str(password), str(user.password)):
        token = token_service.set_token({'email': email})
        # Allowed
        return {'message': MSG_LOGIN, 'token': token, 'http_code_status': 200}

    else:
        # Forbidden
        return {'message': MSG_LOGIN_ERROR, 'http_code_status': 403}


def login_ver_2(username, password, ip):
    pass

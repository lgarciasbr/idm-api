import bcrypt
from flask import abort
from idManager.model.service import account_service
from idManager.model.service import token_service
from idManager.settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSN_400, MSG_LOGOUT, MSG_INVALID_TOKEN, MSG_VALID_TOKEN, \
    MSN_EXPECTED_CONTENT_TYPE_JSON, MSN_EXPECTED_JSON_DATA, MSN_INVALID_API_VER


def check_header(header):
    content_type = header.get('Content-Type')

    if content_type == 'application/json' or content_type == '' or not content_type:
        return True
    else:
        # Bad Request
        abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)


# region LOGIN
def auth_login(header, data):
    check_header(header)

    if not data:
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account, errors = account_service.account_schema_post.load(data)
    if errors:
        abort(400, errors)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_login_ver_1(account["email"], account["password"])
    # elif header['ver'] == '2':
    #    return get_ver_2(username, password, ip)
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


def auth_login_ver_1(email, password):

    account = account_service.get_account(email)

    if account is not None and account.password == bcrypt.hashpw(password.encode('utf-8'), account.password):
        token = token_service.set_token(token_service.generate_token(account), account)
        # Allowed
        return {'message': MSG_LOGIN, 'token': token, 'http_status_code': 200}
    else:
        # Forbidden
        return {'message': MSG_LOGIN_ERROR, 'http_status_code': 403}


def login_ver_2(username, password, ip):
    pass

# endregion


# region LOGOUT
def auth_logout(header):
    check_header(header)

    ver = header.get('ver')
    token = header.get('token')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_logout_ver_1(token)
    # elif header['ver'] == '2':
    #    return auth_logout()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


def auth_logout_ver_1(token):
    if token is not None:
        user_id = token_service.verify_token(token)

        if user_id is not None:
            token_service.delete_token(token)
            # Logout
            return {'message': MSG_LOGOUT, 'token': token, 'http_status_code': 200}
        else:
            # Forbidden
            return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_status_code': 403}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_status_code': 400}


def logout_ver_2(token, ip):
    pass

# endregion


# region Is token valid?
# todo Criar test para o is_valid_token
# todo Com o timeout do login implementado o is_valid_token pode fazer um refresh no timeout.
def auth_is_valid(header):
    check_header(header)

    ver = header.get('ver')
    token = header.get('token')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_is_valid_ver_1(token)
    # elif header['ver'] == '2':
    #    return auth_logout()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


def auth_is_valid_ver_1(token):
    if token is not None:
        user_id = token_service.verify_token(token)

        if user_id is not None:
            # Allowed
            return {'message': MSG_VALID_TOKEN, 'token': token, 'http_status_code': 200}
        else:
            # Forbidden
            return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_status_code': 403}
    else:
        # Forbidden
        return {'message': MSG_INVALID_TOKEN, 'token': token, 'http_status_code': 400}

# endregion

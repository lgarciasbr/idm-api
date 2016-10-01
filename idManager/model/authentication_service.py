from flask import abort
from idManager.model import token_service
from idManager.model import account_service
from idManager.settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSG_LOGOUT, MSG_VALID_TOKEN, \
    MSN_EXPECTED_JSON_DATA, MSN_INVALID_API_VER


# region LOGIN
def auth_login(header, data):
    if not data:
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account, errors = account_service.register_account_schema.load(data)
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
    valid_password, account = account_service.validate_account_password(email, password)

    if valid_password:
        token = token_service.set_token(account)
        # Allowed
        return {'message': MSG_LOGIN,
                'token': token,
                'http_status_code': 200}
    else:
        # Forbidden
        abort(403, MSG_LOGIN_ERROR)


# endregion


# region LOGOUT
@idManager.model.token_service.validate_token
def auth_logout(header):
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
        token_service.delete_token(token)
        # Logout
        return {'message': MSG_LOGOUT,
                'token': token,
                'http_status_code': 200}
# endregion


# region Is token valid?
# todo Com o timeout do login implementado o is_valid_token pode fazer um refresh no timeout.
@idManager.model.token_service.validate_token
def auth_is_valid(header):
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
            # Allowed
            return {'message': MSG_VALID_TOKEN,
                    'token': token,
                    'http_status_code': 200}

# endregion

from flask import abort, current_app
from idManager.model import token_service
from idManager.model import account_service
from idManager.settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSG_LOGOUT, MSG_VALID_TOKEN, \
    MSN_EXPECTED_JSON_DATA, MSN_INVALID_API_VER


# region LOGIN
def auth_login(ver, account_data):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_login_ver_1(account_data["email"], account_data["password"])
    # elif header['ver'] == '2':
    #    return get_ver_2(username, password, ip)
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('auth_login, 400: ' + MSN_INVALID_API_VER)
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
        current_app.extensions['sentry'].captureMessage('auth_login_ver_1, 403: ' + MSG_LOGIN_ERROR)
        abort(403, MSG_LOGIN_ERROR)


# endregion


# region LOGOUT
@token_service.validate_token
def auth_logout(ver, token):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_logout_ver_1(token)
    # elif header['ver'] == '2':
    #    return auth_logout()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('auth_logout, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


def auth_logout_ver_1(token):
        token_service.delete_token(token)
        # Logout
        return {'message': MSG_LOGOUT,
                'token': token,
                'http_status_code': 200}
# endregion


# region Is token valid?
@token_service.validate_token
def auth_is_valid(ver, token):

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return auth_is_valid_ver_1(token)
    # elif header['ver'] == '2':
    #    return auth_logout()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('auth_is_valid, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


def auth_is_valid_ver_1(token):
            # Allowed
            return {'message': MSG_VALID_TOKEN,
                    'token': token,
                    'http_status_code': 200}

# endregion

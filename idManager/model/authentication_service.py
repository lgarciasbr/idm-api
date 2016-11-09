from flask import abort
from idManager.model import token_service, account_service, message_service
from idManager.settings import MSG_LOGIN, MSG_LOGIN_ERROR, MSG_LOGOUT, MSG_VALID_TOKEN


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
        message_service.send_log_message('auth_login_ver_1, 403: ' + MSG_LOGIN_ERROR)
        abort(403, MSG_LOGIN_ERROR)


def auth_logout_ver_1(token):
        token_service.delete_token(token)
        # Logout
        return {'message': MSG_LOGOUT,
                'token': token,
                'http_status_code': 200}


def auth_is_valid_ver_1(token):
            # Allowed
            return {'message': MSG_VALID_TOKEN,
                    'token': token,
                    'http_status_code': 200}

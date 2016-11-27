import functools
import datetime
from flask import request
from idManager.model.integration import token_data
from idManager.model import message_service
from idManager.model.database.db_schema import TokenSchema
from idManager.settings import SECRET_KEY, MSG_INVALID_TOKEN, TOKEN_TIMEOUT
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature)

# region Schema
token_schema = TokenSchema(only=('token',))
verify_token_schema = TokenSchema(only=('token', 'last_accessed_date'))
# endregion


def set_token(account):
    s = Serializer(SECRET_KEY)
    token = (s.dumps(account.id)).decode('ascii')

    if token_data.set_token(account, token):
        return token
    else:
        return None


def get_token_last_accessed_date(account_id, token):
    return token_data.get_token_last_accessed_date(account_id, token)


def get_account_id_from_token(token):
    s = Serializer(SECRET_KEY)
    try:
        account_id = s.loads(token)
    except BadSignature:
        # Forbidden - BadSignature, it is not a valid token.
        message_service.error_403('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)

    return account_id


# Decorator
def validate_token(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        token = request.headers.get('token')

        if token is not None:
            account_id = get_account_id_from_token(token)
            last_accessed_date = get_token_last_accessed_date(account_id, token)

            if last_accessed_date:
                if (datetime.datetime.now() - last_accessed_date).total_seconds() < TOKEN_TIMEOUT:
                    token_data.change_last_accessed_date(account_id, token)
                    result = f(*args, **kwargs)
                else:
                    # Forbidden - TimeOut
                    message_service.error_403('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)
            else:
                # Forbidden - Not registered on DB
                message_service.error_403('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)
        else:
            # No token? Forbidden too ...
            message_service.error_400('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)

        return result

    return wrapped


def delete_token(token):
    account_id = get_account_id_from_token(token)

    return token_data.delete_token(account_id, token)


def delete_token_by_account_id(pk):
    return token_data.delete_token_by_account_id(pk)

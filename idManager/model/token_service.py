import functools
from flask import request
from idManager.model.integration import token_data
from idManager.model import message_service
from idManager.model.database.db_schema import TokenSchema
from idManager.settings import SECRET_KEY, MSG_INVALID_TOKEN
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

# region Schema
token_schema = TokenSchema(only=('token',))
verify_token_schema = TokenSchema(only=('token', 'last_accessed_date'))
# endregion


def set_token(account, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = (s.dumps(account.id)).decode('ascii')

    if token_data.set_token(account, token):
        token_registered = get_token(token)
        return token_schema.dump(token_registered)
    else:
        return None


def get_token(token):
    return token_data.get_token(token)


# Decorator
def validate_token(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        token = request.headers.get('token')

        if token is not None:
            s = Serializer(SECRET_KEY)
            try:
                account_id = s.loads(token)
            # except SignatureExpired:
            #    return False  # valid token, but expired
            except BadSignature:
                # Forbidden
                message_service.error_403('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)

            registered_token = get_token(token)

            if registered_token is None or registered_token.account_id != account_id:
                # Forbidden
                message_service.error_403('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)
            else:
                token_data.change_last_accessed_date(token)
                result = f(*args, **kwargs)
                # result['token'] = verify_token_schema.dump(registered_token)
        else:
            # Forbidden too ...
            message_service.error_400('validate_token: ' + MSG_INVALID_TOKEN, MSG_INVALID_TOKEN)

        return result

    return wrapped


def delete_token(token):
    return token_data.delete_token(token)


def delete_token_by_account_id(pk):
    return token_data.delete_token_by_account_id(pk)

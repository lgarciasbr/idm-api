from idManager.model.integration import token_data
from idManager.settings import SECRET_KEY
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


def set_token(account, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = (s.dumps(account.id)).decode('ascii')

    if token_data.set_token(token, account):
        return token
    else:
        return None


def get_token(token):
    return token_data.get_token(token)


def verify_token(token):
    s = Serializer(SECRET_KEY)
    try:
        account_id = s.loads(token)
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token

    registered_token = get_token(token)

    if registered_token is None or registered_token.account_id != account_id:
        return False  # valid token, but different user
    else:
        return True


def delete_token(token):
    return token_data.delete_token(token)


def delete_token_by_account_id(pk):
    return token_data.delete_token_by_account_id(pk)

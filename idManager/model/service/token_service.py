from idManager.model.integration import token_data
from idManager.settings import SECRET_KEY
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


def set_token(account, expiration=600):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = (s.dumps(account.id)).decode('ascii')

    return token_data.set_token(token, account)


def get_token(token):
    return token_data.get_token(token)


def verify_token(token):
    s = Serializer(SECRET_KEY)
    try:
        account_id = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    account_id_registered_token = get_token(token)

    if account_id_registered_token is None or account_id_registered_token != account_id:
        return None  # valid token, but different user

    return account_id


def delete_token(token):
    return token_data.delete_token(token)


# todo Implementar o timeout do login, precisa pensar nas regras.
# todo preparar unittest do token

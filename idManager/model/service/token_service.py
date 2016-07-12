from idManager.model.integration import token_data
from idManager.settings import SECRET_KEY
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


# todo Implementar o timeout do login, precisa pensar nas regras.
def generate_token(account, expiration):
    s = Serializer(SECRET_KEY, expires_in=expiration)

    return (s.dumps(account.id)).decode('ascii')


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


#todo preparar unittest do token
def get_token(token):
    return token_data.get_token(token)


def set_token(account, expiration=600):
    token = generate_token(account, expiration)

    return token_data.set_token(token, account)


def delete_token(token):
    return token_data.delete_token(token)

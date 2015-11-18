import uuid
from Authentication.model.data import token_data


#todo preprar unittest do token
def get_token_number():
    return uuid.uuid4().__str__()


def get_token(email):
    return token_data.get_token(email)


def set_token(value):
    token = get_token_number()
    token_data.set_token(token, value)
    return token


def delete_token(token):
    return token_data.delete_token(token)

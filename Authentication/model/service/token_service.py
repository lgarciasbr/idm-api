import uuid
from Authentication.model.data import token_data


#todo preprar unittest do token
def generate_token_number():
    return uuid.uuid4().__str__()


def get_token(token):
    return token_data.get_token(token)


def set_token(value):
    return token_data.set_token(generate_token_number(), value)


def delete_token(token):
    return token_data.delete_token(token)

from Authentication.model.data import token_data


#todo preprar unittest do token
def get_token(token):
    return token_data.get_token(token)


def set_token(token, user):
    return token_data.set_token(token, user)


def delete_token(token):
    return token_data.delete_token(token)

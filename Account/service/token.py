from Account.data.memcached import delete_memcached, set_memcached, get_memcached
from config import TOKEN_HOST

import uuid

#todo preprar unittest do token
def get_token_number():
    return uuid.uuid4().__str__()


def get_token(key):
    if TOKEN_HOST == 'memcached':
        return get_memcached(key)
    else:
        #todo implementar get_token com banco de dados
        pass


def set_token(value):
    if TOKEN_HOST == 'memcached':
        token = get_token_number()
        set_memcached(token, value)
        return token
    else:
        #todo implementar set_token com banco de dados
        pass


def delete_token(key):
    if TOKEN_HOST == 'memcached':
        return delete_memcached(key)
    else:
        #todo implementar delete_token com banco de dados
        pass

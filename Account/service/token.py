from Account.data.memcached import delete_memcached, set_memcached, get_memcached


def get_token(key):
    return get_memcached(key)


def set_token(key, value):
    return set_memcached(key, value)


def delete_token(key):
    return delete_memcached(key)

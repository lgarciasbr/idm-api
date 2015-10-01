from flask import json
from pymemcache.client import Client
from config import MEMCACHED_HOST, MEMCACHED_PORT, MSG_INVALID_SERIALIZATION


# JSon
def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return json.loads(value)
    raise Exception(MSG_INVALID_SERIALIZATION )


# Memcached
def get_memcached(key):
    client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)
    return client.get(key)


def set_memcached(key, value):
    client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)
    client.set(key, value)

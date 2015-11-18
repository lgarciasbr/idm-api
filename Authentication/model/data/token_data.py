from pymemcache.client import Client

from lib.json import json_serializer, json_deserializer
from config import MEMCACHED_HOST, MEMCACHED_PORT


#todo criar os unittests do memcached
def get_memcached(key):
    client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)
    return client.get(key)


def set_memcached(key, value):
    value.email
    client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)
    client.set(key, value)


def delete_memcached(key):
    client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)
    return client.delete(key)

from flask import json
from config import MSG_INVALID_SERIALIZATION


# JSon
#todo preparar unittest do Json
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
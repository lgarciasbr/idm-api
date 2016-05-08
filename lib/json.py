from flask import json
from settings import MSG_INVALID_SERIALIZATION


# JSon
#todo preparar unittest do Json
#todo verificar se o jsonify do flask nao substitui esta biblioteca
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

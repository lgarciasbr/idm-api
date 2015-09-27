import json
from pymemcache.client.base import Client
from flask import Flask, jsonify

app = Flask(__name__)


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return json.loads(value)
    raise Exception('Unknown serialization format')


client = Client(('192.168.99.100', 32777), serializer=json_serializer, deserializer=json_deserializer)
client.set('key', {'a':'Hello Memcached!', 'b':'Hello JSon!', 'c':'\o/'})
result = client.get('key')


@app.route('/')
def hello_world():
    try:
        return jsonify(result), 200
    except ValueError as e:
        return e.message, 500

app.debug = True
app.run()

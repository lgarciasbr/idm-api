__author__ = 'leandro'

from flask import Flask
from pymemcache.client.base import Client

app = Flask(__name__)

client = Client(('192.168.99.100/', 32777))
client.set('some_key', " \o/ Hello Memcached!")
result = client.get('some_key')

@app.route("/")
def hello_world():
    return result, 200

app.run()
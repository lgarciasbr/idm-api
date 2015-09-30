import json
from pymemcache.client.base import Client
from flask import Flask, jsonify, make_response, url_for, request
import uuid

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


@app.route('/login', methods=['POST'])
def login():
    try:
        value = request.json
        if request.headers['Content-Type'] == 'application/json' and value['username'] == 'admin' and value['password'] == 'default':
            return 'You were logged in ' + uuid.uuid4().__str__(), 200
    except:
        pass

    return 'Invalid username or password', 403


@app.route('/logout')
def logout():
    return 'You were logged out', 200


@app.errorhandler(404)
def not_found(error):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

'''

        try:
            user_submission = json.loads(request.data)
        except ValueError:
            return Response(status=405)


# Coloca a url do retorno no JSon, interessante para facilitar o retorno para o dev.
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

'''


#app.debug = True
app.run()
from flask import Flask, jsonify, request
from Account.util import get_memcached, set_memcached, delete_memcached
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSG_LOGIN, MSG_LOGOUT, MSG_INVALID_TOKEN, MSN_404, MSG_LOGIN_ERROR

import uuid

#todo como eu mostro so o usuario que foi deslogado?
#todo capturar a url que o servico esta rodando.
#todo colocar as acoes dos endpoints em outros arquivos e trabalhar versao.

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'Project': PROJECT_NAME, 'Description': PROJECT_DESCRIPTION}), 200


@app.route('/login', methods=['POST'])
def login():
    try:
        value = request.json

        if request.headers['Content-Type'] == 'application/json' and \
                value['username'] == 'admin' and \
                value['password'] == 'default':

            token = uuid.uuid4().__str__()

            set_memcached(token, {'Token': token, 'Username': value['username']})

            return jsonify({'Message': MSG_LOGIN, 'Token': token}), 200

    except:
        pass

    return MSG_LOGIN_ERROR, 403


@app.route('/logout', methods=['POST'])
def logout():
    try:
        user = get_memcached(request.headers['token'])

        if user is not None:
            delete_memcached(request.headers['token'])
            return jsonify({'Message': MSG_LOGOUT, 'User': user}), 200

    except:
        pass

    return jsonify({'Message': MSG_INVALID_TOKEN, 'Token': request.headers['token']}), 403


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': MSN_404 + request.url
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

# app.debug = True
app.run()

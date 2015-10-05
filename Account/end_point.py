from flask import Flask, jsonify, request
from Account.service.login import login_v1
from Account.service.token import get_token, delete_token
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSG_LOGOUT, MSG_INVALID_TOKEN, \
    MSN_404, MSG_LOGIN_ERROR, MSN_405

# todo colocar as acoes dos endpoints em outros arquivos e trabalhar versao.

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION}), 200


# todo precisa funcionar mesmo sem a versao
@app.route('/login', methods=['POST'])
def login():
    try:
        value = request.json

        if request.headers['ver'] == 1 and request.headers['Content-Type'] == 'application/json':
            return login_v1(value['username'], value['password'])
        elif request.headers['Content-Type'] == 'application/json':
            # Always use last version here.
            return login_v1(value['username'], value['password'])
        else:
            pass
    except:
        pass

    return jsonify({'message': MSG_LOGIN_ERROR}), 403


@app.route('/logout', methods=['POST'])
def logout():
    if request.headers['ver'] == '1' and request.headers['Content-Type'] == 'application/json':
        try:
            user = get_token(request.headers['token'])

            if user is not None:
                delete_token(request.headers['token'])
                return jsonify({'message': MSG_LOGOUT}), 200

        except:
            pass

    return jsonify({'message': MSG_INVALID_TOKEN, 'token': request.headers['token']}), 403


'''
# Coloca a url do retorno no JSon, interessante para facilitar o retorno para o dev. Usar para a lista de usuarios.
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


# Error
@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': MSN_404 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(405)
def not_allowed(error):
    message = {
        'status': 405,
        'message': MSN_405 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 405

    return resp

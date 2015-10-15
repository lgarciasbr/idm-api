from flask import Flask, jsonify, request
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSN_404, MSN_405, MSN_400
from Account.controller import login_controller, logout_controller

# todo colocar as acoes dos endpoints em outros arquivos e trabalhar versao.

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION}), 200


@app.route('/login', methods=['POST'])
def login():
    return login_controller(request.headers, request.json)


@app.route('/logout', methods=['POST'])
def logout():
    return logout_controller(request.headers, request.json)


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
@app.errorhandler(400)
def not_found(error):
    message = {
        'status': 400,
        'message': MSN_400 + request.url
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

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

from Account import view
from flask import Flask, jsonify, request
from Account.model.service import login_service, logout_service
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSN_404, MSN_405, MSN_400

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION}), 200


@app.route('/login', methods=['POST'])
def login():
    response = login_service.login(request.headers, request.json)
    http_code_status = response.get('http_code_status')
    return view.message_json(response), http_code_status


@app.route('/logout', methods=['POST'])
def logout():
    response = logout_service.logout(request.headers)
    http_code_status = response.get('http_code_status')
    return view.message_json(response), http_code_status

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
def bad_request(error):
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

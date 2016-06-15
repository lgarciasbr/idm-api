from flask import request, Blueprint
from Account import view
from Account.model.service import account_service

account_blueprint = Blueprint('accounts', __name__)


def account_get_email(email):
    return account_service.get_user_by_email(email)


@account_blueprint.route('/accounts', methods=['POST'])
def account_register():
    response = account_service.register(request.headers, request.json)
    http_code_status = response.get('http_code_status')

    return view.message_json(response), http_code_status


@account_blueprint.route('/accounts', methods=['GET'])
def account_get():
    response = account_service.get(request.headers)
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

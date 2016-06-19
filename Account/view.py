from flask import jsonify


# todo implementar o retorno com xml
def account_register(message):
    return jsonify({'message': message})


def account_get(message):
    return jsonify({'users': message.data})

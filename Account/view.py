from flask import jsonify


# todo implementar o retorno com xml
def message_json(value):
    if 'http_code_status' in value:
        del value['http_code_status']

    return jsonify(value)

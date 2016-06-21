from flask import jsonify

# todo implementar o retorno com xml


def message_json(value):
    if 'http_status_code' in value:
        del value['http_status_code']

    return jsonify(value)

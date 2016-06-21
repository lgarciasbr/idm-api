from flask import jsonify


def not_found(e):
    response = jsonify({'status': 404, 'error': 'not found',
                        'message': e.description})
    response.status_code = 404
    return response


def bad_request(e):
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': e.description})
    response.status_code = 400
    return response

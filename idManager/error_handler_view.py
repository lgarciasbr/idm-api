from flask import jsonify
from idManager.settings import MSN_400, MSN_403, MSN_404


def not_found(e):
    response = jsonify({'status_code': 404, 'error': MSN_404,
                        'message': e.description})
    response.status_code = 404
    return response


def forbidden(e):
    response = jsonify({'status_code': 403, 'error': MSN_403,
                        'message': e.description})
    response.status_code = 403
    return response


def bad_request(e):
    response = jsonify({'status_code': 400, 'error': MSN_400,
                        'message': e.description})
    response.status_code = 400
    return response

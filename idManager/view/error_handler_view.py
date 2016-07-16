from flask import jsonify
from idManager.settings import MSN_400, MSN_403, MSN_404


def not_found(e):
    view = jsonify({'status_code': 404,
                    'error': MSN_404,
                    'message': e.description})

    return view


def forbidden(e):
    view = jsonify({'status_code': 403,
                    'error': MSN_403,
                    'message': e.description})

    return view


def bad_request(e):
    view = jsonify({'status_code': 400,
                    'error': MSN_400,
                    'message': e.description})

    return view

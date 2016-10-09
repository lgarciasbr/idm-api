from flask import jsonify
from idManager.settings import MSN_400, MSN_403, MSN_404, MSN_405, MSN_500


def internal_server_error(e):
    view = jsonify({'status_code': 500,
                    'error': MSN_500,
                    'message': e.description})

    return view


def not_allowed(e):
    view = jsonify({'status_code': 405,
                    'error': MSN_405,
                    'message': e.description})

    return view


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

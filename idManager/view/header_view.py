from functools import wraps
from flask import make_response, abort, request
from idManager.settings import MSN_EXPECTED_CONTENT_TYPE_JSON, MSG_NEWEST_VERSION
from idManager.model import message_service


def add_response_headers(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        ver = request.headers.get('ver')

        if ver == '' or not ver:
            ver = MSG_NEWEST_VERSION

        response = make_response(f(*args, **kwargs))

        header = response.headers

        header['ver'] = ver
        header['Content-Type'] = 'application/json'

        return response

    return wrapper


def verify_content_type(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        content_type = request.headers.get('Content-Type')

        if content_type == 'application/json' or content_type == '' or not content_type:
            result = f(*args, **kwargs)

            return result
        else:
            # Bad Request
            message_service.send_log_message('add_response_headers, 400: ' + MSN_EXPECTED_CONTENT_TYPE_JSON)
            abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)

    return wrapped

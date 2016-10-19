from functools import wraps
from flask import make_response, abort, request, current_app
from idManager.settings import MSN_EXPECTED_CONTENT_TYPE_JSON, MSG_NEWEST_VERSION


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
            current_app.extensions['sentry'].captureMessage('add_response_headers, 400: '
                                                            + MSN_EXPECTED_CONTENT_TYPE_JSON)
            abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)

    return wrapped

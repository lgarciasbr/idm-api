from flask import make_response, request, abort
from idManager.settings import MSN_EXPECTED_CONTENT_TYPE_JSON, MSG_NEWEST_VERSION
from functools import wraps


def add_response_headers(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        content_type = request.headers.get('Content-Type')
        ver = request.headers.get('ver')

        if content_type == 'application/json' or content_type == '' or not content_type:
            if ver == '' or not ver:
                ver = MSG_NEWEST_VERSION

            response = make_response(f(*args, **kwargs))

            header = response.headers

            header['ver'] = ver
            header['Content-Type'] = 'application/json'

            return response
        else:
            # Bad Request
            abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)

    return wrapper

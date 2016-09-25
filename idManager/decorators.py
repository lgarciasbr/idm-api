import functools
from functools import wraps

from flask import make_response, abort, request

from idManager.model import token_service
from idManager.settings import MSG_INVALID_TOKEN, MSN_EXPECTED_CONTENT_TYPE_JSON, MSG_NEWEST_VERSION


def validate(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        token = request.headers.get('token')

        if token is not None:
            if token_service.verify_token(token):
                result = f(*args, **kwargs)

            else:
                abort(403, MSG_INVALID_TOKEN)

        else:
            # Forbidden
            abort(400, MSG_INVALID_TOKEN)

        return result

    return wrapped


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
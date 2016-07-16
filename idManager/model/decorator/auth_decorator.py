import functools
from flask import abort, request
from idManager.model.service import token_service


def validate(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        token = request.headers.get('token')

        if token_service.verify_token(token):
            result = f(*args, **kwargs)
        else:
            abort(403)

        return result

    return wrapped

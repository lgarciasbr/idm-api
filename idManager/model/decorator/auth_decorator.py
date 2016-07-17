import functools
from flask import abort, request
from idManager.model.service import token_service
from idManager.settings import MSG_INVALID_TOKEN


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

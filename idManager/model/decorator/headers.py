from flask import make_response
import functools


def add_response_headers(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        result = make_response(f(*args, **kwargs))

        headers = {'ver': '1', 'Content-Type': 'application/json'}

        h = result.headers
        for header, value in headers.items():
            h[header] = value

        return result

    return wrapped

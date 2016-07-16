import functools


# decorator without arguments
def decorator_name(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        # do work before original function

        result = f(*args, **kwargs)

        # do work after original function
        # modify result if necessary

        return result

    return wrapped


# decorator with arguments
def decorator_name(args):
    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):

            # do work before original function

            result = f(*args, **kwargs)

            # do work after original function
            # modify result if necessary

            return result

        return wrapped

    return decorator

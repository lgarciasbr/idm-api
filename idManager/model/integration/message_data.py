from flask import current_app


def send_log_message(text):
    try:
        current_app.extensions['sentry'].captureMessage(text)
    except:
        pass

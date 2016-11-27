from werkzeug.exceptions import abort

from idManager.model.integration import message_data
from idManager.settings import COLLECT_LOG_ERRORS, MSN_EXPECTED_JSON_DATA, MSN_EXPECTED_ID, MSN_INVALID_API_VER


def send_log_message(text):
    if COLLECT_LOG_ERRORS:
        message_data.send_log_message(text)


def exception(method_name, error):
    send_log_message(method_name + ': ' + error)


def expected_json_data():
    send_log_message('change_account_password, 400: ' + MSN_EXPECTED_JSON_DATA)
    abort(400, MSN_EXPECTED_JSON_DATA)


def expected_id():
    send_log_message('change_account_password, 400: ' + MSN_EXPECTED_ID)
    abort(400, MSN_EXPECTED_ID)


def invalid_api_ver():
    send_log_message('delete_account_by_id, 400: ' + MSN_INVALID_API_VER)
    abort(400, MSN_INVALID_API_VER)


def wrong_json_data(errors):
    send_log_message('account_register, 400: ' + str(errors))
    abort(400, errors)


def error_400(text_log, text_message=''):
    send_log_message('error 400 - ' + text_log)
    abort(400, text_message)


def error_403(text_log, text_message=''):
    send_log_message('error 403 - ' + text_log)
    abort(403, text_message)


def error_404(text_log, text_message=''):
    send_log_message('error 404 - ' + text_log)
    abort(404, text_message)


def error_500(text_log, text_message=''):
    send_log_message('error 500 - ' + text_log)
    abort(500, text_message)
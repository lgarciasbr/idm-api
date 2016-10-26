from idManager.model.integration import message_data
from idManager.settings import COLLECT_LOG_ERRORS


def send_log_message(text):
    if COLLECT_LOG_ERRORS:
        message_data.send_log_message(text)

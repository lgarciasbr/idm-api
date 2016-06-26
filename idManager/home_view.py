from flask import jsonify
from settings import PROJECT_NAME, PROJECT_DESCRIPTION


def home():
    response = jsonify({'status_code': 200, 'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION})
    response.status_code = 200

    return response

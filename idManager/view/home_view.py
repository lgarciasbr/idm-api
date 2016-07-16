from flask import jsonify
from idManager.settings import PROJECT_NAME, PROJECT_DESCRIPTION


def home():
    view = jsonify({'status_code': 200,
                        'project': PROJECT_NAME,
                        'description': PROJECT_DESCRIPTION})

    return view

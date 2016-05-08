from flask import jsonify, Blueprint
from settings import PROJECT_NAME, PROJECT_DESCRIPTION

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def home():
    return jsonify({'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION}), 200

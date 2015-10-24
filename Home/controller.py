from flask import jsonify, Blueprint
from config import PROJECT_NAME, PROJECT_DESCRIPTION

home_blueprint = Blueprint('home', __name__)

# todo montar o view e o model da home


@home_blueprint.route('/')
def home():
    return jsonify({'project': PROJECT_NAME, 'description': PROJECT_DESCRIPTION}), 200

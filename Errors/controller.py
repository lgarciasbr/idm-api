from flask import Blueprint
from Errors import view
from config import MSN_400, MSN_404, MSN_405, MSN_500

error_blueprint = Blueprint('errors', __name__)

# todo criar unittest
@error_blueprint.errorhandler(400)
def bad_request(error):
    response = {'message': MSN_400}
    http_code_status = 400

    return view.message_json(response), http_code_status


@error_blueprint.app_errorhandler(404)
def not_found(error):
    response = {'message': MSN_404}
    http_code_status = 404

    return view.message_json(response), http_code_status


@error_blueprint.errorhandler(405)
def not_allowed(error):
    response = {'message': MSN_405}
    http_code_status = 405

    return view.message_json(response), http_code_status

'''
@error_blueprint.errorhandler(500)
def not_allowed(error):
    response = {'message': MSN_500}
    http_code_status = 500

    return view.message_json(response), http_code_status
'''

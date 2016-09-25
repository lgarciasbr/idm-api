import idManager.decorators
from idManager.view import home_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/')
@idManager.decorators.add_response_headers
def home():
    response = home_view.home()
    response.status_code = 200

    return response

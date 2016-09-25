import idManager.view.header_view
from idManager.view import home_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/')
@idManager.view.header_view.add_response_headers
def home():
    response = home_view.home()
    response.status_code = 200

    return response

from idManager.view import home_view
from . import id_manager_blueprint
from idManager.model.decorator import headers


@id_manager_blueprint.route('/')
@headers.add_response_headers
def home():
    response = home_view.home()
    response.status_code = 200

    return response

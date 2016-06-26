from idManager.view import home_view
from . import id_manager_blueprint


@id_manager_blueprint.route('/')
def home():
    return home_view.home()

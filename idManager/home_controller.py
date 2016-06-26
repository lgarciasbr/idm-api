from . import id_manager_blueprint
from idManager import home_view


@id_manager_blueprint.route('/')
def home():
    return home_view.home()

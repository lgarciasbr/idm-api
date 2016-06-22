from . import account_blueprint
from Account import home_view


@account_blueprint.route('/')
def home():
    return home_view.home()

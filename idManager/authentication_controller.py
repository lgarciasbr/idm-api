from flask import request
from idManager.model.service import authentication_service
from idManager.view import authentication_view
from . import id_manager_blueprint


# todo 2 steps verification - http://blog.miguelgrinberg.com/post/two-factor-authentication-with-flask

@id_manager_blueprint.route('/auth/', methods=['POST'])
def auth_login():
    auth = authentication_service.auth_login(request.headers, request.get_json(force=True, silent=True))
    return authentication_view.auth_login(auth)


@id_manager_blueprint.route('/auth/', methods=['GET'])
def auth_is_valid():
    auth = authentication_service.auth_is_valid(request.headers)
    return authentication_view.auth_is_valid(auth)


@id_manager_blueprint.route('/auth/', methods=['DELETE'])
def auth_logout():
    auth = authentication_service.auth_logout(request.headers)
    return authentication_view.auth_logout(auth)

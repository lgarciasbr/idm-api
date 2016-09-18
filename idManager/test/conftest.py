import pytest
from manage import create_app


@pytest.fixture(scope='session')
def app():
    app_test = create_app('idManager.settings')
    return app_test


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

import pytest
from manage import create_app


@pytest.fixture(scope='session')
def app():
    app_test = create_app('idManager.settings')
    return app_test


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()


'''
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

from idManager.model.database.db_model import db as Base # This is your declarative base class


def setup_module():
    global transaction, connection, engine

    # Connect to the database and create the schema within a transaction
    engine = create_engine('postgresql://postgres:Scr33nN3t@localhost:5432/lgidm_test')
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(connection)

    # If you want to insert fixtures to the DB, do it here


def teardown_module():
    # Roll back the top level transaction and disconnect from the database
    transaction.rollback()
    connection.close()
    engine.dispose()


class DatabaseTest(object):
    def setup(self):
        self.__transaction = connection.begin_nested()
        self.session = Session(connection)

    def teardown(self):
        self.session.close()
        self.__transaction.rollback()
'''
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from idManager import id_manager_blueprint
from idManager.model.database.db_model import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(id_manager_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.directory = './idManager/model/database/migrations'

    return app


def app_default(self, arg1):
    app = create_app('idManager.settings')

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    @manager.command
    def test():
        import pytest

        pytest.main("-x idManager/test")

    return manager


if __name__ == "__main__":
    manager = app_default()
    manager.run()

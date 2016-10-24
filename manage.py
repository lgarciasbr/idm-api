from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from idManager import id_manager_blueprint
from idManager.model.database.db_model import db
from raven.contrib.flask import Sentry
import coverage


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(id_manager_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.directory = './idManager/model/database/migrations'

    # Collect log errors.
    sentry = Sentry()
    sentry.init_app(app)

    return app

app = create_app('idManager.settings')

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    @manager.command
    def test():
        import pytest

        pytest.main("-x tests")

    @manager.command
    def coverage():
        pass
        # coverage run manage.py test
        # coverage xml
        # You can find the token in Project -> Settings -> Integrations -> Project API.
        # export CODACY_PROJECT_TOKEN=f07b3166dff2432d9d6eb0c9ca197334
        # python-codacy-coverage -r coverage.xml

    manager.run()

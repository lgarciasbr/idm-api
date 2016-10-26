from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from idManager import id_manager_blueprint
from idManager.model.database.db_model import db
from raven.contrib.flask import Sentry
import coverage as cov_test
from idManager.settings import COLLECT_LOG_ERRORS


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(id_manager_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.directory = './idManager/model/database/migrations'

    # Collect log errors.
    if COLLECT_LOG_ERRORS:
        sentry = Sentry()
        sentry.init_app(app)

    return app

app = create_app('idManager.settings')

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    @manager.command
    def test():
        """Runs application tests"""
        import pytest

        pytest.main("-x tests")

    @manager.command
    def coverage():
        """Runs coverage tests"""
        cov = cov_test.Coverage()
        cov.start()

        test()

        cov.stop()
        cov.save()
        cov.xml_report()
        cov.report()

        # token = You can find the token in Project -> Settings -> Integrations -> Project API.
        # export CODACY_PROJECT_TOKEN=token
        # python-codacy-coverage -r coverage.xml

    manager.run()

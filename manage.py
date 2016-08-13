import os

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


if __name__ == "__main__":
    app = create_app('idManager.settings')

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()

    @manager.command
    def test():
        """Execute UnitTest."""
        import unittest

        tests = unittest.TestLoader().discover('idManager/test')
        unittest.TextTestRunner(verbosity=2).run(tests)

    @manager.command
    def test_coverage():
        """Execute UnitTest, than create a coverage page."""
        import coverage
        import unittest

        cov = coverage.coverage(
            branch=True,
            include={'idManager/*'}
        )
        cov.start()
        tests = unittest.TestLoader().discover('test')
        unittest.TextTestRunner(verbosity=2).run(tests)
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'coverage')
        cov.html_report(directory=covdir)
        cov.erase()

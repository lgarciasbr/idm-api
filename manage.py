from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

import os
from idManager.account_controller import id_manager_blueprint
from database import db
from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(id_manager_blueprint)

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    'Execute UnitTest.'
    import unittest

    tests = unittest.TestLoader().discover('Test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def test_coverage():
    'Execute UnitTest, than create a coverage page.'
    import coverage
    import unittest

    cov = coverage.coverage(
        branch=True,
        include={'idManager/*'}
    )
    cov.start()
    tests = unittest.TestLoader().discover('Test')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == "__main__":
    manager.run()

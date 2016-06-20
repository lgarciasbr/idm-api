import os
import gunicorn
from flask import Flask
from database import db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from Account.controller import account_blueprint
from Authentication.controller import authentication_blueprint
from Home.controller import home_blueprint

app = Flask(__name__)
app.config.from_object('settings')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(authentication_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(home_blueprint)

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
        include={'Authentication/*', 'Account/*', 'Home/*'}
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

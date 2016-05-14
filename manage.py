import argparse
import os
import gunicorn
from flask import Flask
from database import db
from Account.controller import account_blueprint
from Authentication.controller import authentication_blueprint
from Home.controller import home_blueprint
from Errors.controller import error_blueprint
from settings import BASE_DIR

app = Flask(__name__)
app.config.from_object('settings')

db.init_app(app)

app.register_blueprint(authentication_blueprint)
app.register_blueprint(account_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(error_blueprint)

# todo resolver o problema de criacao do banco.
# todo resolver o problema de upgrade do banco.
if not os.path.isfile(BASE_DIR.child('app.db')):
    with app.app_context():
        db.create_all()


def run_server():
    app.run()


def test():
    import unittest

    tests = unittest.TestLoader().discover('Test')
    unittest.TextTestRunner(verbosity=2).run(tests)


def test_coverage():
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
    option_help = "Choose manage.py runserver or test or test_coverage"

    parser = argparse.ArgumentParser()
    parser.add_argument("option", help=option_help, nargs='?')

    args = parser.parse_args()

    if args.option == 'runserver':
        run_server()
    elif args.option == 'test':
        test()
    elif args.option == 'test_coverage':
        test_coverage()
    else:
        print(option_help)

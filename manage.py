import argparse
import os


def test():
    import unittest

    """Runs the unit tests without coverage."""

    tests = unittest.TestLoader().discover('Test')
    unittest.TextTestRunner(verbosity=2).run(tests)


def test_coverage():
    import coverage
    import unittest

    """Runs the unit tests with coverage."""
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


def run_server():
    from lg_idm import app

    app.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    option_help = "Choose manage.py runserver or test or test_coverage"

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

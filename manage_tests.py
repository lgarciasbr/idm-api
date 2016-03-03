import unittest
import os
import coverage


def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('Test')
    unittest.TextTestRunner(verbosity=2).run(tests)


def cov():
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

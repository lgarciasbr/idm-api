try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Identity Management System',
    'author': 'Leandro Garcia',
    'url': '',
    'download_url': '',
    'author_email': 'leandro.garcias@gmail.com',
    'version': '0.1',
    'install_requires': ['pymemcache', 'flask', 'gunicorn', 'coverage'],
    'packages': ['LG_idM'],
    'scripts': [],
    'name': 'LG idM - LG Identity Management'
}

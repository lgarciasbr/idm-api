try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple account app with Memcached and Postgree',
    'author': 'Leandro Garcia',
    'url': '',
    'download_url': '',
    'author_email': 'leandro.garcias@gmail.com',
    'version': '0.1',
    'install_requires': ['pymemcache', 'flask', 'gunicorn'],
    'packages': ['LG_Account'],
    'scripts': [],
    'name': 'LG_Account'
}

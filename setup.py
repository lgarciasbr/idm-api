#todo arrumar o arquivo de setup, foco nas dependencias
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['pymemcache','flask'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Account'
}

setup(**config, requires=['pymemcache','flask'])
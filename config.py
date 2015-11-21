import os

# Ajuda a verificar se estou rodando local ou na nuvem.
# WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# todo implementar o sistema em mais de um idioma

# Project
PROJECT_NAME = 'Account'
PROJECT_DESCRIPTION = 'Studying Python!'

# Token Host
# Option: memcached, database
TOKEN_HOST = 'database'

# Mencached Host
if os.environ.get('SERVER') is None:
    MEMCACHED_HOST = '192.168.99.100'
    MEMCACHED_PORT = 32777
else:
    # todo documentar que precisa criar as variaveis de ambiente para o memcached
    MEMCACHED_HOST = ''
    MEMCACHED_PORT = ''

# BD
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # postgresql://user:password/mydatabase
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# General Text
MSG_LOGIN = 'You were logged in!'
MSG_LOGIN_ERROR = 'Invalid username or password'
MSG_LOGOUT = 'You were logged out!'
MSG_INVALID_TOKEN = 'Invalid Token!'
MSG_INVALID_SERIALIZATION = 'Unknown serialization format.'
MSG_EMAIL_ALREADY_REGISTERED = 'E-mail is already registered.'
MSG_ACCOUNT_SET = 'Account set!'

# Error
MSN_400 = 'Bad Request'
MSN_404 = 'Not Found'
MSN_405 = 'The method is not allowed!'
MSN_500 = 'Sorry, we encountered an error while trying to fulfill your request.'

# Test
EMAIL_TEST = 'admin@admin.com'
PWD_TEST = 'default'

'''
# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
'''

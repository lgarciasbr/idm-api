import os

# Ajuda a verificar se estou rodando local ou na nuvem.
# WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# Project
PROJECT_NAME = 'Account'
PROJECT_DESCRIPTION = 'Studying Python!'

# Token
# Option: memcached, postgres
# todo implementar o token via banco.
TOKEN_HOST = 'memcached'

if os.environ.get('SERVER') is None:
    MEMCACHED_HOST = '192.168.99.100'
    MEMCACHED_PORT = 32777
else:
    # todo documentar que precisa criar as variaveis de ambiente para o memcached
    MEMCACHED_HOST = ''
    MEMCACHED_PORT = ''

# General Text
MSG_LOGIN = 'You were logged in!'
MSG_LOGIN_ERROR = 'Invalid username or password'
MSG_LOGOUT = 'You were logged out!'
MSG_INVALID_TOKEN = 'Invalid Token!'
MSG_INVALID_SERIALIZATION = 'Unknown serialization format'

# Error
MSN_404 = 'Not found: '
MSN_405 = 'The method is not allowed for '

'''
# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
'''

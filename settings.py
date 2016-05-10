import os
from decouple import config

# todo implementar o sistema em mais de um idioma
# todo implementar a biblioteca do Henrique Bastos para a configuracao .env
# todo ALLOWED_HOSTS, Secret Key,
# todo Verificar como buscar foto de perfil, igual os sites fazem hoje, voce cadastra e aparece sua foto.

DEBUG = config('DEBUG', default=False, cast=bool)
# Token Host - option: memcached, database
TOKEN_HOST = config('TOKEN_HOST', default='database')
# Memcahed
MEMCACHED_SERVERS = config('MEMCACHED_HOST', default='localhost:11211')
MEMCACHED_USERNAME = config('MEMCACHED_USERNAME', default='')
MEMCACHED_PASSWORD = config('MEMCACHED_PASSWORD', default='')
# BD Config
SQLITE_BASEDIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI', default='sqlite:///' + SQLITE_BASEDIR)
# Set to 'False' or True to domain name resolution on email check when register a new account.
CHECK_DELIVERABILITY = config('CHECK_DELIVERABILITY', default=True, cast=bool)

##############

# Project
PROJECT_NAME = 'LG-IdM'
PROJECT_DESCRIPTION = 'Studying Python and CI!'

# General Messages
MSG_LOGIN = 'You were logged in!'
MSG_LOGIN_ERROR = 'Invalid username or password'
MSG_LOGOUT = 'You were logged out!'
MSG_INVALID_TOKEN = 'Invalid Token!'
MSG_VALID_TOKEN = 'Valid Token!'
MSG_INVALID_SERIALIZATION = 'Unknown serialization format.'
MSG_EMAIL_ALREADY_REGISTERED = 'E-mail is already registered.'
MSG_ACCOUNT_SET = 'Account set!'

# Error
MSN_400 = 'Bad Request'
MSN_403 = 'Forbidden'
MSN_404 = 'Not Found'
MSN_405 = 'The method is not allowed!'
MSN_500 = 'Sorry, we encountered an error while trying to fulfill your request.'

# Test
EMAIL_TEST = 'admin@admin.com'
PWD_TEST = 'default'

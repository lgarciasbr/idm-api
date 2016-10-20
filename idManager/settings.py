from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
# Token Host - option: redis, database
TOKEN_HOST = config('TOKEN_HOST', default='database')
# BD Config
DATABASE_URL = config('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DATABASE_URL
# Set to 'False' or True to domain name resolution on email check when register a new account.
CHECK_EMAIL_DELIVERABILITY = config('CHECK_EMAIL_DELIVERABILITY', cast=bool)
# Collect log errors. https://sentry.io
SENTRY_DSN = config('SENTRY_DSN')

##############

# Project
PROJECT_NAME = 'LG-IdM'
PROJECT_DESCRIPTION = 'LG - Identity Manager'

# General Messages
MSG_LOGIN = 'You were logged in!'
MSG_LOGIN_ERROR = 'Invalid username or password'
MSG_LOGOUT = 'You were logged out!'
MSG_INVALID_TOKEN = 'Invalid Token!'
MSG_VALID_TOKEN = 'Valid Token!'
MSG_INVALID_SERIALIZATION = 'Unknown serialization format.'
MSG_EMAIL_ALREADY_REGISTERED = 'E-mail is already registered.'
MSG_ACCOUNT_SET = 'Account set!'
MSG_ACCOUNT_DELETED = 'Account permanently deleted!'
MSG_ACCOUNT_PWD_CHANGED = 'Account password changed!'
MSG_NEWEST_VERSION = 'The newest version!'

# Error Messages
MSN_400 = 'Bad Request'
MSN_403 = 'Forbidden'
MSN_404 = 'Not Found'
MSN_405 = 'The method is not allowed!'
MSN_500 = 'Sorry, we encountered an error while trying to fulfill your request.'
MSN_INVALID_API_VER = 'Invalid API version.'
MSN_EXPECTED_CONTENT_TYPE_JSON = 'Expected Content-Type: application/json'
MSN_EXPECTED_JSON_DATA = 'No input data provided'

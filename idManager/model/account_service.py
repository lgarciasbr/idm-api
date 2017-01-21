import bcrypt
from email_validator import validate_email, EmailNotValidError
from idManager.model import token_service, message_service
from idManager.model.database.db_schema import AccountSchema
from idManager.model.integration import account_data
from idManager.model.util_service import pagination
from idManager.settings import MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY, \
    MSG_ACCOUNT_DELETED, MSG_ACCOUNT_PWD_CHANGED

# region Schema
register_account_schema = AccountSchema(only=('email', 'password'))
change_account_password_schema = AccountSchema(only=('password', 'new_password'))
get_account_schema = AccountSchema(only=('email', 'url', 'created_at', 'id'))
get_accounts_schema = AccountSchema(many=True, only=('id','email', 'url'))
# endregion


def crypt_pwd(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def validate_account_password(email, password):
    account = account_data.get_account_by_email(email)

    if account is not None and account.password == bcrypt.hashpw(password.encode('utf-8'), account.password):
        return True, account
    else:
        return False, None


def account_register_ver_1(email, password):
    try:
        # e-mail validation and get info
        v = validate_email(email, check_deliverability=CHECK_EMAIL_DELIVERABILITY)
        # replace with normalized form
        email = v["email"]
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        message_service.error_400('account_register_ver_1: ' + str(e), str(e))

    account = account_data.get_account_by_email(email)

    if account is None:
        if account_data.register_account(email, crypt_pwd(password)):
            account = account_data.get_account_by_email(email)

            return {'message': MSG_ACCOUNT_SET,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 201}
        else:
            message_service.error_500('account_register_ver_1')

    else:
        message_service.error_403('account_register_ver_1: ' + MSG_EMAIL_ALREADY_REGISTERED, MSG_EMAIL_ALREADY_REGISTERED)


def change_account_password_ver_1(pk, password, new_password):
    # Find account by ID
    account = account_data.get_account_by_id(pk)

    if account is not None:
        # Verify if this password belongs to this account
        valid_pwd, account = validate_account_password(account.email, password)

        if valid_pwd:
            account_data.change_account_password(pk, crypt_pwd(new_password))
            return {'message': MSG_ACCOUNT_PWD_CHANGED,
                    'http_status_code': 202}
        else:
            message_service.error_403('change_account_password_ver_1')
    else:
        message_service.error_404('change_account_password_ver_1')


def get_accounts_ver_1(page, per_page):
    accounts = account_data.get_accounts(page, per_page)

    pages = pagination(accounts, page, per_page)

    return {'accounts': get_accounts_schema.dump(accounts.items),
            'total': accounts.total,
            'pages': pages,
            'http_status_code': 200}


def get_account_by_id_ver_1(pk):
    account = account_data.get_account_by_id(pk)

    if account is not None:
        return {'account': get_account_schema.dump(account),
                'http_status_code': 200}
    else:
        message_service.error_404('get_account_by_id_ver_1')


def delete_account_by_id_ver_1(pk):
    account = account_data.get_account_by_id(pk)
    if account is not None:
        # Delete all token (auth) from this account first
        token_service.delete_token_by_account_id(pk)

        # Then delete the account.
        if account_data.delete_account_by_id(pk):
            return {'message': MSG_ACCOUNT_DELETED,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 202}
        else:
            message_service.error_500('delete_account_by_id_ver_1')
    else:
        message_service.error_404('delete_account_by_id_ver_1')

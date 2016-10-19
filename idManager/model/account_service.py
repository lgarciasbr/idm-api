import bcrypt
from email_validator import validate_email, EmailNotValidError
from flask import abort, current_app
from idManager.model import token_service
from idManager.model.database.db_schema import AccountSchema
from idManager.model.integration import account_data
from idManager.settings import MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY, \
    MSN_INVALID_API_VER, MSG_ACCOUNT_DELETED, MSG_ACCOUNT_PWD_CHANGED

# region Schema
register_account_schema = AccountSchema(only=('email', 'password'))
change_account_password_schema = AccountSchema(only=('password', 'new_password'))
get_account_schema = AccountSchema(only=('email', 'url', 'created_at', 'id'))
get_accounts_schema = AccountSchema(many=True, only=('email', 'url'))
# endregion


def crypt_pwd(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# TODO Precisa testar para verificar se o sistema esta diferenciando maiuscula de minuscula.
# TODO PRECISA CRIAR UMA SOLUCAO PARA REGRAS DE SENHA. Ex.: uma maiscula e etc. Olhar o AD para ver como funciona.
# TODO COLOCAR O SCRETKEY NA EQUACAO PARA SENHA??
def validate_account_password(email, password):
    account = account_data.get_account_by_email(email)

    if account is not None and account.password == bcrypt.hashpw(password.encode('utf-8'), account.password):
        return True, account
    else:
        return False, None


# region Register_Account
def account_register(ver, account_data):
    # Use 'or not ver' at the last version
    if ver == '1' or not ver:
        return account_register_ver_1(account_data["email"], account_data["password"])
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('account_register, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


def account_register_ver_1(email, password):
    try:
        # e-mail validation and get info
        v = validate_email(email, check_deliverability=CHECK_EMAIL_DELIVERABILITY)
        # replace with normalized form
        email = v["email"]
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        current_app.extensions['sentry'].captureMessage('account_register_ver_1, 400: ' + str(e))
        abort(400, str(e))

    account = account_data.get_account_by_email(email)

    if account is None:
        if account_data.register_account(email, crypt_pwd(password)):
            account = account_data.get_account_by_email(email)

            return {'message': MSG_ACCOUNT_SET,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 201}
        else:
            current_app.extensions['sentry'].captureMessage('account_register_ver_1, 500')
            abort(500)

    else:
        current_app.extensions['sentry'].captureMessage('account_register_ver_1, 403: ' + MSG_EMAIL_ALREADY_REGISTERED)
        abort(403, MSG_EMAIL_ALREADY_REGISTERED)
# endregion


# region Change_Account_Password
@token_service.validate_token
def change_account_password(ver, account_password, pk):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return change_account_password_ver_1(pk, account_password['password'], account_password['new_password'])
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('change_account_password, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


def change_account_password_ver_1(pk, password, new_password):
    # Find account by ID
    account = account_data.get_account_by_id(pk)

    if account is not None:
        # Verify if this password belongs to this account
        valid_pwd, account = validate_account_password(account.email, password)

        if valid_pwd:
            account_data.change_account_password(pk, crypt_pwd(new_password))
            return {'message': MSG_ACCOUNT_PWD_CHANGED,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 202}
        else:
            current_app.extensions['sentry'].captureMessage('change_account_password_ver_1, 403')
            abort(403)
    else:
        current_app.extensions['sentry'].captureMessage('change_account_password_ver_1, 404')
        abort(404)
# endregion


# TODO Verificar se ele pertence ao grupo de ADMIN
# region Get_Accounts
@token_service.validate_token
def get_accounts(ver):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return get_accounts_ver_1()
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('get_accounts, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


def get_accounts_ver_1():
    accounts = account_data.get_accounts()
    return {'accounts': get_accounts_schema.dump(accounts),
            'http_status_code': 200}
# endregion


# TODO Verificar se ele pertence ao grupo de ADMIN ou se ele e ele mesmo.
# region Get_Account_By_Id
@token_service.validate_token
def get_account_by_id(ver, pk):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return get_account_by_id_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('get_account_by_id, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def get_account_by_id_ver_1(pk):
    account = account_data.get_account_by_id(pk)

    if account is not None:
        return {'account': get_account_schema.dump(account),
                'http_status_code': 200}
    else:
        current_app.extensions['sentry'].captureMessage('get_account_by_id_ver_1, 404')
        abort(404)
# endregion


# TODO Se nao for o admin pedir senha
# region Delete_Account_By_Id
@token_service.validate_token
def delete_account_by_id(ver, pk):
    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return delete_account_by_id_ver_1(pk)
    # elif header['ver'] == '2':
    #    return delete_account_by_id_ver_2()
    else:
        # Bad Request
        current_app.extensions['sentry'].captureMessage('delete_account_by_id, 400: ' + MSN_INVALID_API_VER)
        abort(400, MSN_INVALID_API_VER)


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
            current_app.extensions['sentry'].captureMessage('delete_account_by_id_ver_1, 500')
            abort(500)
    else:
        current_app.extensions['sentry'].captureMessage('delete_account_by_id_ver_1, 404')
        abort(404)
# endregion

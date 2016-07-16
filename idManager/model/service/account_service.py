import bcrypt
from email_validator import validate_email, EmailNotValidError
from flask import abort
from idManager.model.integration import account_data
from idManager.model.decorator import auth_decorator
from idManager.model.service import token_service
from idManager.model.database.db_schema import AccountSchema
from idManager.settings import MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY, MSN_INVALID_API_VER, \
    MSN_EXPECTED_CONTENT_TYPE_JSON, MSN_EXPECTED_JSON_DATA, MSG_ACCOUNT_DELETED, MSG_ACCOUNT_PWD_CHANGED

# region Schema
register_account_schema = AccountSchema(only=('email', 'password'))
change_account_password_schema = AccountSchema(only=('password', 'new_password'))
get_account_schema = AccountSchema(only=('email', 'url', 'created_at', 'id'))
get_accounts_schema = AccountSchema(many=True, only=('email', 'url'))

# endregion


def check_header(header):
    content_type = header.get('Content-Type')

    if content_type == 'application/json' or content_type == '' or not content_type:
        return True
    else:
        # Bad Request
        abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)


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
def account_register(header, data):
    check_header(header)

    if not data:
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account, errors = register_account_schema.load(data)
    if errors:
        abort(400, errors)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return account_register_ver_1(account["email"], account["password"])
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


def account_register_ver_1(email, password):
    try:
        # e-mail validation and get info
        v = validate_email(email, check_deliverability=CHECK_EMAIL_DELIVERABILITY)
        # replace with normalized form
        email = v["email"]
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        abort(400, str(e))

    account = account_data.get_account_by_email(email)

    if account is None:
        if account_data.register_account(email, crypt_pwd(password)):
            account = account_data.get_account_by_email(email)

            return {'message': MSG_ACCOUNT_SET,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 201}
        else:
            abort(500)

    else:
        abort(403, MSG_EMAIL_ALREADY_REGISTERED)
# endregion


# region Change_Account_Password
@auth_decorator.validate
def change_account_password(header, data, pk):
    check_header(header)

    if not data or not pk:
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account_password, errors = change_account_password_schema.load(data)
    if errors:
        abort(400, errors)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return change_account_password_ver_1(pk, account_password['password'], account_password['new_password'])
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


def change_account_password_ver_1(pk, password, new_password):
    # Find account by ID
    account = account_data.get_account_by_id(pk)

    if account is not None:
        # Verify if this password belongs to this account
        valid_pwd = validate_account_password(account.email, password)

        if valid_pwd:
            account_data.change_account_password(pk, crypt_pwd(new_password))
            return {'message': MSG_ACCOUNT_PWD_CHANGED,
                    'account': get_account_schema.dump(account),
                    'http_status_code': 202}
        else:
            abort(403)
    else:
        abort(404)

# endregion


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN
# region Get_Accounts
@auth_decorator.validate
def get_accounts(header):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return get_accounts_ver_1()
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def get_accounts_ver_1():
    accounts = account_data.get_accounts()
    return {'accounts': get_accounts_schema.dump(accounts),
            'http_status_code': 200}
# endregion


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN ou se ele e ele mesmo.
# region Get_Account_By_Id
@auth_decorator.validate
def get_account_by_id(header, pk):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return get_account_by_id_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def get_account_by_id_ver_1(pk):
    account = account_data.get_account_by_id(pk)

    if account is not None:
        return {'account': get_account_schema.dump(account),
                'http_status_code': 200}
    else:
        abort(404)
# endregion


# TODO Precisa apagar todas as sessoes do usuario antes de apagar o usuario.
# region Delete_Account_By_Id
@auth_decorator.validate
def delete_account_by_id(header, pk):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return delete_account_by_id_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
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
            abort(500)
    else:
        abort(404)
# endregion


# todo retornar a versao da api que foi chamada.

import bcrypt
from email_validator import validate_email, EmailNotValidError
from flask import abort
from idManager.model.integration import account_data
from idManager.settings import MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY, MSN_INVALID_API_VER, \
    MSN_EXPECTED_CONTENT_TYPE_JSON, MSN_EXPECTED_JSON_DATA, MSG_ACCOUNT_DELETED

account_schema_post = account_data.account_schema_post


def check_header(header):
    content_type = header.get('Content-Type')

    if content_type == 'application/json' or content_type == '' or not content_type:
        return True
    else:
        # Bad Request
        abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)


# todo deixar estas duas func genericas
def get_account(email):
    return account_data.get_account(email)


def get_account_by_id(pk):
    return account_data.get_account_by_id(pk)


# region Register
def account_register(header, data):
    check_header(header)

    if not data:
        abort(400, MSN_EXPECTED_JSON_DATA)

    # Validate Schema
    account, errors = account_schema_post.load(data)
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


# TODO PRECISA CRIAR UMA SOLUCAO PARA REGRAS DE SENHA. Ex.: uma maiscula e etc. Olhar o AD para ver como funciona.
# TODO CRIAR OS TESTES DO REGISTER
# TODO COLOCAR O SCRETKEY NA EQUACAO PARA SENHA
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

    if account is None or len(account.data) == 0:
        # register
        if account_data.register_account(email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())):
            account = account_data.get_account_by_email(email)

            return {'message': MSG_ACCOUNT_SET, 'account': account, 'http_status_code': 201}
        else:
            abort(500)

    else:
        abort(403, MSG_EMAIL_ALREADY_REGISTERED)


# endregion


# region Accounts_Get
# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN
def accounts_get(header):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return accounts_get_ver_1()
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def accounts_get_ver_1():
    return {'message': account_data.get_accounts(), 'http_status_code': 200}

# endregion


# region Account_Get
# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN ou se ele e ele mesmo.
def account_get(header, pk):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return account_get_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def account_get_ver_1(pk):
    account = account_data.get_account_by_id(pk)

    if account is not None and len(account.data) != 0:
        return {'message': account, 'http_status_code': 200}
    else:
        abort(404)

# endregion


# region Delete
def account_delete(header, pk):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or not ver:
        return account_delete_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO Precisa apagar todas as sessoes do usuario antes de apagar o usuario.
def account_delete_ver_1(pk):
    account = account_data.get_account_by_id(pk)

    if account is not None or len(account.data) != 0:
        if account_data.delete_account(pk):
            return {'message': MSG_ACCOUNT_DELETED, 'account': account, 'http_status_code': 202}
        else:
            abort(500)
    else:
        abort(404)


# endregion


# todo retornar a versao da api que foi chamada.

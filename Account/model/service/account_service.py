from Account.model.data import account_data
from settings import MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY, MSN_INVALID_API_VER, \
    MSN_EXPECTED_CONTENT_TYPE_JSON, MSN_EXPECTED_JSON_DATA
from email_validator import validate_email, EmailNotValidError
from flask import abort
import bcrypt


def check_header(header):
    content_type = header.get('Content-Type')

    if content_type == 'application/json' or content_type == '' or content_type is None:
        return True
    else:
        # Bad Request
        abort(400, MSN_EXPECTED_CONTENT_TYPE_JSON)


def get_user_by_email(email):
    return account_data.get_first(email)

# region Register


def register(header, data):
    check_header(header)

    if not data:
        abort(400, MSN_EXPECTED_JSON_DATA)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or ver is None:
        return register_ver_1(data["email"], data["password"])
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO PRECISA CRIAR UMA SOLUCAO PARA REGRAS DE SENHA. Ex.: uma maiscula e etc. Olhar o AD para ver como funciona.
# TODO CRIAR OS TESTES DO REGISTER
def register_ver_1(email, password):
    try:
        # e-mail validation and get info
        v = validate_email(email, check_deliverability=CHECK_EMAIL_DELIVERABILITY)
        # replace with normalized form
        email = v["email"]
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        abort(403, str(e))

    # if e-mail is not registered
    if not get_user_by_email(email):
        # register
        account_data.register(email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))

        return {'message': MSG_ACCOUNT_SET, 'http_status_code': 200}
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
    if ver == '1' or ver is None:
        return accounts_get_ver_1()
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def accounts_get_ver_1():
    return {'message': account_data.accounts_get(), 'http_status_code': 200}

# endregion


# region Account_Get


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN ou se ele e ele mesmo.
def account_get(header, pk):
    check_header(header)

    ver = header.get('ver')

    # Use 'or ver is None' at the last version
    if ver == '1' or ver is None:
        return account_get_ver_1(pk)
    # elif header['ver'] == '2':
    #    return get_ver_2()
    else:
        # Bad Request
        abort(400, MSN_INVALID_API_VER)


# TODO CRIAR OS TESTES DO GET
def account_get_ver_1(pk):
    account = account_data.account_get(pk)

    if len(account.data) != 0:
        return {'message': account, 'http_status_code': 200}
    else:
        abort(404)

# endregion

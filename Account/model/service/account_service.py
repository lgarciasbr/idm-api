from Account.model.data import user_data
from settings import MSN_400, MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY
from email_validator import validate_email, EmailNotValidError
from flask import abort
import bcrypt


def get_user_by_email(email):
    return user_data.get_first(email)

# region Register


def register(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return register_ver_1(data["email"], data["password"])
            # elif header['ver'] == '2':
            #    return login_ver_2()
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


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
        return {'message': str(e), 'http_code_status': 403}

    # if e-mail is not registered
    if not get_user_by_email(email):
        # register
        user_data.register(email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))

        return {'message': MSG_ACCOUNT_SET, 'http_code_status': 200}
    else:
        return {'message': MSG_EMAIL_ALREADY_REGISTERED, 'http_code_status': 403}


# endregion


# region Accounts_Get


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN
def accounts_get(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return accounts_get_ver_1()
            # elif header['ver'] == '2':
            #    return get_ver_2()
    except Exception:
        pass

    # Bad Request
    abort(400)


# TODO CRIAR OS TESTES DO GET
def accounts_get_ver_1():
    return {'message': user_data.accounts_get(), 'http_code_status': 200}

# endregion


# region Account_Get


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN
def account_get(header, pk):
    content_type = header.get('Content-Type')
    ver = header.get('ver')

    # todo no heroku nao e content_type == ''
    if content_type == 'application/json' or content_type == '':
        # Use 'or ver is None' at the last version
        if ver == '1' or ver is None:
            return account_get_ver_1(pk)
        # elif header['ver'] == '2':
        #    return get_ver_2()
        else:
            # Bad Request
            abort(400, 'Invalid API version.')
    else:
        # Bad Request
        abort(400, 'Expected Content-Type: application/json')


# TODO CRIAR OS TESTES DO GET
def account_get_ver_1(pk):
    account = user_data.account_get(pk)

    if len(account.data) != 0:
        return {'message': account, 'http_code_status': 200}
    else:
        abort(404)

# endregion

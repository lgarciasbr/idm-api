from Account.model.data import user_data
from settings import MSN_400, MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY
from email_validator import validate_email, EmailNotValidError
import bcrypt


from flask import url_for


class ValidationError(ValueError):
    pass


def get_url(self):
    return url_for('api.get_customer', id=self.id, _external=True)


def import_data(self, data):
    try:
        self.email = data['email']
    except KeyError as e:
        raise ValidationError('Invalid: missing ' + e.args[0])
    return self


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


# region Get


# TODO Verificar se o token e valido.
# TODO Verificar se ele pertence ao grupo de ADMIN
def get(header):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return get_ver_1()
            # elif header['ver'] == '2':
            #    return get_ver_2()
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


# TODO CRIAR OS TESTES DO GET
def get_ver_1():
    return {'message': user_data.get(), 'http_code_status': 200}

# endregion

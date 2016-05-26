from Account.model.data import user_data
from settings import MSN_400, MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET, CHECK_EMAIL_DELIVERABILITY
from email_validator import validate_email, EmailNotValidError
import bcrypt


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
        # validate and get info
        v = validate_email(email, check_deliverability=CHECK_EMAIL_DELIVERABILITY)
        # replace with normalized form
        email = v["email"]
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return {'message': str(e), 'http_code_status': 403}

    if not get_user_by_email(email):
        user_data.register(email, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))

        return {'message': MSG_ACCOUNT_SET, 'http_code_status': 200}
    else:
        return {'message': MSG_EMAIL_ALREADY_REGISTERED, 'http_code_status': 403}


def get_user_by_email(email):
    return user_data.get_user(email)

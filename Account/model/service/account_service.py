from Account.model.data import user_data
from config import MSN_400, MSG_EMAIL_ALREADY_REGISTERED, MSG_ACCOUNT_SET
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


# TODO CRIAR OS TESTES DO REGISTER
def register_ver_1(email, password):
    if not get_user_by_email(email):
        user_data.register(email, bcrypt.hashpw(str(password), bcrypt.gensalt()))

        return {'message': MSG_ACCOUNT_SET, 'http_code_status': 200}
    else:
        return {'message': MSG_EMAIL_ALREADY_REGISTERED, 'http_code_status': 403}


# TODO CRIAR OS TESTES para check email
def get_user_by_email(email):
    return user_data.get_user(email)

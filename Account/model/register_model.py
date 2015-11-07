from database import db, User
# from Account.model.data.account import User
from config import MSN_400


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


def register_ver_1(email, password):
    db.session.add(User(email, password))
    db.session.commit()

    return {'message': 'Ok', 'http_code_status': 200}

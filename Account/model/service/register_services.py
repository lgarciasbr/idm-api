from config import MSN_400


def register(header, data):
    try:
        if header['Content-Type'] == 'application/json':
            if header['ver'] == '1':
                return register_ver_1()
            # elif header['ver'] == '2':
            #    return login_ver_2()
    except Exception:
        pass

    # Bad Request
    return {'message': MSN_400, 'http_code_status': 400}


def register_ver_1():

    # todo implementar a chamada via banco de dados
        # Login
        return {'message': MSN_400, 'http_code_status': 200}

# postgresql://scott:tiger@localhost/mydatabase

# postgresql://scott:tiger@localhost/mydatabase

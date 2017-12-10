import json
from tests import util

PWD_TEST = 'default'


# region Header variables
def header_empty():
    return {}


def header_content_type():
    return {'Content-Type': 'application/json'}


def header_empty_content_type():
    return {'Content-Type': ''}


def header_invalid_content_type():
    return {'Content-Type': 'invalid'}


def header_content_type_ver():
    return {'Content-Type': 'application/json', 'ver': '1'}


def header_no_content_type_ver():
    return {'ver': '1'}


def header_content_type_no_ver():
    return {'Content-Type': 'application/json'}


def header_empty_content_type_ver():
    return {'Content-Type': '', 'ver': '1'}


def header_content_type_empty_ver():
    return {'Content-Type': 'application/json', 'ver': ''}


def header_invalid_content_type_ver():
    return {'Content-Type': 'invalid', 'ver': '1'}


def header_content_type_invalid_ver():
    return {'Content-Type': 'application/json', 'ver': '888'}
# endregion


# region Data Body variable
def data_empty():
    return {}


def data_email_pwd():
    return {'email': util.generate_random_email(), 'password': PWD_TEST}


# I hope 'NotExistDomain1974.com' do not exist. ;-)
def data_deliverability_email_pwd():
    return {'email': 'admin13@NotExistDomain1974.com', 'password': PWD_TEST}


def data_no_email_pwd():
    return {'password': PWD_TEST}


def data_empty_email_pwd():
    return {'email': '', 'password': PWD_TEST}


def data_invalid_email_pwd():
    return {'email': 'invalid e-mail', 'password': PWD_TEST}


def data_email_empty_pwd():
    return {'email': util.generate_random_email(), 'password': ''}


def data_email_no_pwd():
    return {'email': util.generate_random_email()}
# endregion


# region Get Token, Account ID and etc.
def register_account(client):
    headers = header_content_type_ver()
    data = data_email_pwd()

    response_register = client.post('/accounts/',
                                    headers=headers,
                                    data=json.dumps(data)
                                    )

    try:
        pk_value = json.loads(response_register.data.decode('utf-8'))['account']['_id']
    except:
        pass

    return data, headers, pk_value


def auth_login(client, data, headers):
    response_login = client.post('/auth/',
                                 headers=headers,
                                 data=json.dumps(data)
                                 )
    token_value = json.loads(response_login.data.decode('utf-8'))['_token']
    return token_value
# endregion

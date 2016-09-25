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
    return {'email': 'admin@NotExistDomain1974.com', 'password': PWD_TEST}


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

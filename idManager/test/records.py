from idManager.settings import EMAIL_TEST, PWD_TEST


# region Header variables
header_empty = {}

header_content_type = {'Content-Type': 'application/json'}

header_empty_content_type = {'Content-Type': ''}

header_invalid_content_type = {'Content-Type': 'invalid'}

header_content_type_ver = {'Content-Type': 'application/json',
                           'ver': '1'}

header_no_content_type_ver = {'ver': '1'}

header_content_type_no_ver = {'Content-Type': 'application/json'}

header_empty_content_type_ver = {'Content-Type': '',
                                 'ver': '1'}

header_content_type_empty_ver = {'Content-Type': 'application/json',
                                 'ver': ''}

header_invalid_content_type_ver = {'Content-Type': 'invalid',
                                   'ver': '1'}

header_content_type_invalid_ver = {'Content-Type': 'application/json',
                                   'ver': '888'}
# endregion

# region Data Body variable
data_empty = {}

data_email_pwd = {'email': EMAIL_TEST,
                  'password': PWD_TEST}

# I hope 'NotExistDomain1974.com' do not exist. ;-)
data_deliverability_email_pwd = {'email': 'admin@NotExistDomain1974.com',
                                 'password': PWD_TEST}

data_no_email_pwd = {'password': PWD_TEST}

data_empty_email_pwd = {'email': '',
                        'password': PWD_TEST}

data_invalid_email_pwd = {'email': 'invalid e-mail',
                          'password': PWD_TEST}

data_email_empty_pwd = {'email': EMAIL_TEST,
                        'password': ''}

data_email_no_pwd = {'email': EMAIL_TEST}
# endregion

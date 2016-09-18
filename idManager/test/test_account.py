import json
import pytest
from idManager.test import records


# region Register_Account
# todo Precisa tratar o banco de dados / limpar os dados ou criar um e-mail diferente a cada vez.
# todo Precisa resolver o teste do deliverability do e-mail.
@pytest.mark.parametrize(("header", "data", "deliverability", "expected"), [
    (records.header_empty(), records.data_email_pwd(), False, 201),
    (records.header_no_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_no_ver(), records.data_email_pwd(), False, 201),
    (records.header_empty_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_empty_ver(), records.data_email_pwd(), False, 201),
    (records.header_invalid_content_type_ver(), records.data_email_pwd(), False, 400),
    (records.header_content_type_invalid_ver(), records.data_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_deliverability_email_pwd(), True, 400),
    (records.header_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_ver(), records.data_empty(), False, 400),
    (records.header_content_type_ver(), records.data_no_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_empty_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_invalid_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_email_no_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_email_empty_pwd(), False, 400),
])
def test_register_account(client, header, data, deliverability, expected):
    #app.config['CHECK_EMAIL_DELIVERABILITY'] = deliverability
    #settings.CHECK_EMAIL_DELIVERABILITY = deliverability

    response = client.post('/accounts/',
                           headers=header,
                           data=json.dumps(data))

    assert response.status_code == expected


def test_register_a_registered_account(client):
    headers = records.header_content_type_ver()
    data = records.data_email_pwd()

    client.post('/accounts/',
                headers=headers,
                data=json.dumps(data)
                )

    response_second = client.post('/accounts/',
                                  headers=headers,
                                  data=json.dumps(data)
                                  )

    assert response_second.status_code == 403
# endregion


# todo Token errado e pk errado
@pytest.mark.parametrize(("header", "token", "pk", "expected"), [
    (records.header_empty(), True, True, 202),
    (records.header_empty(), False, True, 400),
    (records.header_empty(), True, False, 405),
    (records.header_empty(), False, False, 405),
    (records.header_no_content_type_ver(), True, True, 202),
    (records.header_no_content_type_ver(), False, True, 400),
    (records.header_no_content_type_ver(), True, False, 405),
    (records.header_no_content_type_ver(), False, False, 405),
    (records.header_content_type_no_ver(), True, True, 202),
    (records.header_content_type_no_ver(), False, True, 400),
    (records.header_content_type_no_ver(), True, False, 405),
    (records.header_content_type_no_ver(), False, False, 405),
    (records.header_empty_content_type_ver(), True, True, 202),
    (records.header_empty_content_type_ver(), False, True, 400),
    (records.header_empty_content_type_ver(), True, False, 405),
    (records.header_empty_content_type_ver(), False, False, 405),
    (records.header_content_type_empty_ver(), True, True, 202),
    (records.header_content_type_empty_ver(), False, True, 400),
    (records.header_content_type_empty_ver(), True, False, 405),
    (records.header_content_type_empty_ver(), False, False, 405),
    (records.header_invalid_content_type_ver(), True, True, 400),
    (records.header_invalid_content_type_ver(), False, True, 400),
    (records.header_invalid_content_type_ver(), True, False, 405),
    (records.header_invalid_content_type_ver(), False, False, 405),
    (records.header_content_type_invalid_ver(), True, True, 400),
    (records.header_content_type_invalid_ver(), False, True, 400),
    (records.header_content_type_invalid_ver(), True, False, 405),
    (records.header_content_type_invalid_ver(), False, False, 405),
    (records.header_content_type_ver(), True, True, 202),
    (records.header_content_type_ver(), False, True, 400),
    (records.header_content_type_ver(), True, False, 405),
    (records.header_content_type_ver(), False, False, 405),
])
def test_delete_account_by_id(client, header, token, pk, expected):
    headers = records.header_content_type_ver()
    data = records.data_email_pwd()

    if pk or token:
        response_register = client.post('/accounts/',
                                        headers=headers,
                                        data=json.dumps(data)
                                        )

    if pk:
        pk_value = json.loads(response_register.data.decode('utf-8'))['account']['_id']
    else:
        pk_value = ''

    if token:
        response_login = client.post('/auth/',
                                     headers=headers,
                                     data=json.dumps(data)
                                     )

        token_value = json.loads(response_login.data.decode('utf-8'))['auth']['_token']

        header['token'] = token_value

    response_delete = client.delete('/accounts/' + str(pk_value),
                                    headers=header)

    assert response_delete.status_code == expected


def change_account_password(pk, header, data):
    # Change Password
    # PUT http://127.0.0.1:5000/accounts/38

    try:
        response = requests.put(
            url="http://127.0.0.1:5000/accounts/" + pk,
            headers=header,
            data=json.dumps(data)
        )
        print('change_account_password')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('change_account_password - HTTP Request failed!')
        return None


def get_accounts(header):
    # Get Users
    # GET http://127.0.0.1:5000/accounts/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/",
            headers=header
        )
        print('get_accounts')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('get_accounts - HTTP Request failed!')
        return None


def get_account_by_id(pk, header):
    # Get User
    # GET http://127.0.0.1:5000/accounts/38

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/" + pk,
            headers=header
        )
        print('get_account_by_id')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('get_account_by_id - HTTP Request failed!')
        return None

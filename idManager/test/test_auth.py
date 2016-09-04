from flask import request as requests, jsonify as json


def auth_login(header, data):
    # Login
    # POST http://127.0.0.1:5000/auth/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
            data=json.dumps(data)
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_login - HTTP Request failed!')
        return None


def auth_is_valid(header):
    # Is this token valid?
    # GET http://127.0.0.1:5000/auth/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
        )
        print('auth_is_valid')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_is_valid - HTTP Request failed!')
        return None


def auth_logout(header):
    # Logout
    # DELETE http://127.0.0.1:5000/auth/

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
        )
        print('auth_logout')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_logout - HTTP Request failed!')
        return None

# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Welcome
    # GET http://127.0.0.1:5000/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/",
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Register
    # POST http://127.0.0.1:5000/accounts/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/accounts/",
            headers={
                "ver": "1",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "annalee.drago@officedomain.com",
                "password": "default"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Login
    # POST http://127.0.0.1:5000/auth/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/auth/",
            headers={
                "ver": "1",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "sunshine.carreiro@freemail.de",
                "password": "default"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Change Password
    # PUT http://127.0.0.1:5000/accounts/38

    try:
        response = requests.put(
            url="http://127.0.0.1:5000/accounts/38",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "new_password": "default8",
                "password": "default"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Get Users
    # GET http://127.0.0.1:5000/accounts/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Get User
    # GET http://127.0.0.1:5000/accounts/38

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/38",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Is this token valid?
    # GET http://127.0.0.1:5000/auth/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/auth/",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Logout
    # DELETE http://127.0.0.1:5000/auth/

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/auth/",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Login Duplicate
    # POST http://127.0.0.1:5000/auth/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/auth/",
            headers={
                "ver": "1",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "sunshine.carreiro@freemail.de",
                "password": "default8"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Change Password Duplicate
    # PUT http://127.0.0.1:5000/accounts/38

    try:
        response = requests.put(
            url="http://127.0.0.1:5000/accounts/38",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUxNiwiZXhwIjoxNDY5MzY3MTE2fQ.Mzg.Mcsl7BSyUq5xw7BqIDR8bQsD0suR8y4jKvHbf9xwyYU",
                "ver": "1",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "new_password": "default8",
                "password": "errado"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Delete User
    # DELETE http://127.0.0.1:5000/accounts/38

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/accounts/38",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUxNiwiZXhwIjoxNDY5MzY3MTE2fQ.Mzg.Mcsl7BSyUq5xw7BqIDR8bQsD0suR8y4jKvHbf9xwyYU",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Delete User (wrong token)
    # DELETE http://127.0.0.1:5000/accounts/38

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/accounts/38",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Is this token valid? (wrong token)
    # GET http://127.0.0.1:5000/auth/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/auth/",
            headers={
                "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ2OTM2NjUwOCwiZXhwIjoxNDY5MzY3MTA4fQ.Mzg.F9mEKe1dzn5jJxl8VhpfoLUTtO3ICk6CcBQqeF3D3Ag",
                "ver": "1",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



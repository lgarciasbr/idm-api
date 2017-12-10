## idM - Identity Manager

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.org/lgarciasbr/idm-api.svg?branch=master)](https://travis-ci.org/lgarciasbr/idm-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c01f4786068422e9b50575b30f60373)](https://www.codacy.com/app/leandro-garcias/idm-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lgarciasbr/idm-api&amp;utm_campaign=Badge_Grade)

"Identity management describes the management of individual identities, their authentication, authorization, roles and privileges within or across system and enterprise boundaries with the goal of increasing security and productivity while decreasing cost, downtime, and repetitive tasks."
[Wikipedia](https://en.wikipedia.org/wiki/Identity_management_system)

Project RoadMap - https://trello.com/b/DJvDqM1d/mindstorm

### Development Environment

You'll need the following for your development environment:

1. [Python 3.5](http://www.python.org/)
2. [PostgreSQL](https://www.postgresql.org/)
3. [Redis](http://redis.io/)
4. [Sentry](https://sentry.io)

### Local Setup

#### 1. Clone the project:

```console
git clone https://github.com/lgarciasbr/idm-api.git
cd idm-api
```

#### 2. Create and initialize virtualenv for the project:

OSX or Linux
```console
python -m venv .idm-api
source .idm-api/bin/activate
pip install -r requirements.txt
```

Windows
```console
python -m venv .idm-api
.idm-api\Scripts\activate
pip install -r requirements.txt
```

#### 3. Configure your project, use *ini* or *.env*:

OSX or Linux
```console
cp contrib/.env-sample .env
```

Windows
```console
copy contrib/settings-sample.ini settings.ini
```

Obs.: Use environment variables on production.

### Management Commands

#### 1. Create or upgrade database tables:

```console
python manage.py db upgrade
```

#### 2. Test your project:

```console
python manage.py test
```

Other project management commands can be listed with the following command:

```console
python manage.py
```

#### 3. Run your project:

```console
python manage.py runserver
```

##

About me - https://about.me/leandro.garcias

## LG-IdM - LG Identity Management

[ ![Codeship Status for lgarciasbr/lg-idm](https://codeship.com/projects/875dd1c0-6694-0133-fcc4-72bdfd530753/status?branch=master)](https://codeship.com/projects/113803)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ae7d8519e3cd459ab55bd82d16136056)](https://www.codacy.com/app/leandro-garcias/lg-idm?utm_source=lgarciasbr@bitbucket.org&amp;utm_medium=referral&amp;utm_content=lgarciasbr/lg-idm&amp;utm_campaign=Badge_Grade)

"Identity management (IdM) describes the management of individual identities, their authentication, authorization, roles and privileges within or across system and enterprise boundaries with the goal of increasing security and productivity while decreasing cost, downtime, and repetitive tasks."
[Wikipedia](https://en.wikipedia.org/wiki/Identity_management_system)

Why?

SOMETHING HERE

Project RoadMap - https://trello.com/b/DJvDqM1d/mindstorm

### Development Environment

You'll need the following for your development environment:

1. [Python 3.5](http://www.python.org/)
2. [PostgreSQL](https://www.postgresql.org/)
3. [Redis](http://redis.io/)

### Local Setup

#### 1. Clone the project:

```console
git clone https://lgarciasbr@bitbucket.org/lgarciasbr/lg-idm.git lg-idm
cd lg-idm
```

#### 2. Create and initialize virtualenv for the project:

OSX or Linux
```console
python -m venv .lg-idm
source .lg-idm/bin/activate
pip install -r requirements-dev.txt
```

Windows
```console
python -m venv .lg-idm
.lgidm\Scripts\activate
pip install -r requirements-dev.txt
```

#### 3. Configure your project, use *ini* or *.env*:

OSX or Linux
```console
cp contrib/env-sample .env
```

Windows
```console
cp contrib/settings-sample.ini settings.ini
```

Obs.: Use environment variables on production.

### Management Commands

The project management commands can be listed with the following command:

```console
python manage.py
```

#### 1. Create or upgrade database tables:

```console
python manage.py db upgrade
```

#### 2. Test your project:

```console
python manage.py test
```


#### 3. Run your project:

```console
python manage.py runserver
```

# LG-IdM - LG Identity Management

Sistema de Eventos encomendado pela Morena.

[ ![Codeship Status for lgarciasbr/lg-idm](https://codeship.com/projects/875dd1c0-6694-0133-fcc4-72bdfd530753/status?branch=master)](https://codeship.com/projects/113803)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.


```console
git clone https://lgarciasbr@bitbucket.org/lgarciasbr/lg-idm.git lg-idm
cd lg-idm
python -m venv .lg-idm
source .lg-idm/bin/activate
pip install -r requirements-dev.txt
python manage.py test
```

## Como fazer o deploy?

1. Crie um instância no heroku.
2. Envie o código para o heroku
3. Teste.


```console
heroku create minhainstancia
git push heroku master --force
heroku open
```
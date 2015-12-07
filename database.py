from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO Precisa testar para verificar se o sistema esta diferenciando maiuscula de minuscula.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80), unique=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return {'e-mail': self.email}


# todo precisa tirar a coluna email e colocar um id_user
class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), unique=False)
    email = db.Column(db.String(120), unique=False)

    def __init__(self, token, email):
        self.token = token
        self.email = email

    def __repr__(self):
        return {'token': self.token}

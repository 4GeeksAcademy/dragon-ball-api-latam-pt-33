from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
        self.is_active = True

    def __repr__(self):
        return '<Usuario %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach,
            "username": self.username
        }

class Character(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(42), unique=True, nullable=False)
    ki = db.Column(db.Integer, nullable=False)
    race = db.Column(db.String(48), nullable=False)

    def __init__(self, name, ki, race):
        self.name = name
        self.ki = ki
        self.race = race

    def serialize(self):
        return {
            'name': self.name,
            'ki': self.ki,
            'race': self.race
        }

class Favorite(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)

    def serialize(self):

        return {
            'id': self.id
        }
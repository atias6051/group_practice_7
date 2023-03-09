from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Coulmn(db.Integer, nullable=False)
    defense = db.Coulmn(db.Integer, nullable=False)
    image_url = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False, unique=True)
    type = db.Column(db.String(), nullable=False)
    moves = db.Column(db.String(), nullable=False)
    encounter_rate = db.Column(db.Float)
    catch_rate = db.Column(db.Float)
    captured = db.Column(db.Boolean)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)

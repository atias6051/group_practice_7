from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), db.ForeignKey("pokemon_types.type"), nullable=False)
    moves = db.Column(db.String(), nullable=False)
    encounter_rate = db.Column(db.Float)
    catch_rate = db.Column(db.Float)
    captured = db.Column(db.Boolean)

    items = db.relationship("Item", back_populates="pokemon", cascade="all,delete")

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageUrl": self.image_url,
            "name": self.name,
            "type": self.type,
            "moves": list(self.moves.split(',')),
            "encounter_rate": self.encounter_rate,
            "catch-rate": self.catch_rate,
            "captured": self.captured
        }


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)

    pokemon = db.relationship("Pokemon", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "imageUrl": self.image_url,
            "name": self.name,
            "price": self.price,
            "pokemonId": self.pokemonId
        }


class PokemonType(db.Model):
    __tablename__ = 'pokemon_types'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }

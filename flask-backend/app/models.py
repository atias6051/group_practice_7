from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = "pokemon_table"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(
        db.String, db.ForeignKey("pokemon_types_table.type"), nullable=False
    )
    moves = db.Column(db.String, nullable=False)
    encounter_rate = db.Column(db.Float, nullable=False)
    catch_rate = db.Column(db.Float, nullable=False)
    captured = db.Column(db.Boolean, nullable=False)

    items = db.relationship("Item", back_populates="pokemon")
    types = db.relationship("PokemonType", back_populates="pokemon")

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "image_url": self.image_url,
            "name": self.name,
            "attack": self.attack,
            "defense": self.defense,
            "type": self.type,
            "moves": (self.moves).split(", "),
            "encounter_rate": self.encounter_rate,
            "catch_rate": self.catch_rate,
            "captured": self.captured,
        }


class Item(db.Model):
    __tablename__ = "items_table"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemon_table.id"), nullable=False)

    pokemon = db.relationship("Pokemon", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "image_url": self.image_url,
            "name": self.name,
            "price": self.price,
            "pokemonId": self.pokemonId,
        }


class PokemonType(db.Model):
    __tablename__ = "pokemon_types_table"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=True, nullable=False)

    pokemon = db.relationship("Pokemon", back_populates="types")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
        }

from ..models import db, PokemonType
from sqlalchemy import text
def seed_pokemon_type_table():
    normal = PokemonType(type="normal")
    electric= PokemonType(type="electric")
    fire= PokemonType(type="fire")
    psychic = PokemonType(type="psychic")
    ghost = PokemonType(type="ghost")
    water = PokemonType(type="water")
    bug = PokemonType(type="bug")
    dragon= PokemonType(type="dragon")
    grass= PokemonType(type="grass")
    fighting= PokemonType(type="fighting")
    ice= PokemonType(type="ice")
    flying= PokemonType(type="flying")
    poison= PokemonType(type="poison")
    ground= PokemonType(type="ground")
    rock= PokemonType(type="rock")
    steel= PokemonType(type="steel")

    db.session.add_all([normal, electric, fire, psychic, ghost, water, bug,
                       dragon, grass, fighting, ice, flying, poison, ground, rock, steel])
    db.session.commit()

def undo_pokemon_type_table():
    db.session.execute("DELETE from pokemon_types")
    db.session.commit()
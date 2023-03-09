from app.models import db, PokemonType


def seed_pokemon_types():
    pt1 = PokemonType(
        type="fire",
    )
    pt2 = PokemonType(type="electric")
    pt3 = PokemonType(type="normal")
    pt4 = PokemonType(type="ghost")
    pt5 = PokemonType(type="psychic")
    pt6 = PokemonType(type="water")
    pt7 = PokemonType(type="bug")
    pt8 = PokemonType(type="dragon")
    pt9 = PokemonType(type="grass")
    pt10 = PokemonType(type="fighting")
    pt11 = PokemonType(type="ice")
    pt12 = PokemonType(type="flying")
    pt13 = PokemonType(type="poison")
    pt14 = PokemonType(type="ground")
    pt15 = PokemonType(type="rock")
    pt16 = PokemonType(type="steel")

    db.session.add_all(
        [
            pt1,
            pt2,
            pt3,
            pt4,
            pt5,
            pt6,
            pt7,
            pt8,
            pt9,
            pt10,
            pt11,
            pt12,
            pt13,
            pt14,
            pt15,
            pt16,
        ]
    )
    db.session.commit()


def undo_pokemon_types():
    db.session.execute("DELETE FROM pokemon_types")
    db.session.commit()

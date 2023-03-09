from app.models import db, Pokemon


def seed_pokemon():
    p1 = Pokemon(
        number=1,
        image_url="/images/pokemon_snaps/1.svg",
        name="Bulbasaur",
        attack=49,
        defense=49,
        type="grass",
        moves="tackle, vine whip",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p2 = Pokemon(
        number=2,
        image_url="/images/pokemon_snaps/2.svg",
        name="Ivysaur",
        attack=62,
        defense=63,
        type="grass",
        moves="tackle, vine whip, razor leaf",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p3 = Pokemon(
        number=3,
        image_url="/images/pokemon_snaps/3.svg",
        name="Venusaur",
        attack=82,
        defense=83,
        type="grass",
        moves="tackle, vine whip, razor leaf",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p4 = Pokemon(
        number=4,
        image_url="/images/pokemon_snaps/4.svg",
        name="Charmander",
        attack=52,
        defense=43,
        type="fire",
        moves="scratch, ember, metal claw",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p5 = Pokemon(
        number=5,
        image_url="/images/pokemon_snaps/5.svg",
        name="Charmeleon",
        attack=64,
        defense=58,
        type="fire",
        moves="scratch, ember, metal claw, flamethrower",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p6 = Pokemon(
        number=6,
        image_url="/images/pokemon_snaps/6.svg",
        name="Charizard",
        attack=84,
        defense=78,
        type="fire",
        moves="flamethrower, wing attack, slash, metal claw",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p7 = Pokemon(
        number=7,
        image_url="/images/pokemon_snaps/7.svg",
        name="Squirtle",
        attack=48,
        defense=65,
        type="water",
        moves="tackle, bubble, water gun",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=True,
    )
    p8 = Pokemon(
        number=8,
        image_url="/images/pokemon_snaps/8.svg",
        name="Wartortle",
        attack=63,
        defense=80,
        type="water",
        moves="tackle, bubble, water gun, bite",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=False,
    )
    p9 = Pokemon(
        number=9,
        image_url="/images/pokemon_snaps/9.svg",
        name="Blastoise",
        attack=83,
        defense=100,
        type="water",
        moves="hydro pump, bubble, water gun, bite",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=False,
    )
    p10 = Pokemon(
        number=10,
        image_url="/images/pokemon_snaps/10.svg",
        name="Caterpie",
        attack=30,
        defense=35,
        type="bug",
        moves="tackle",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=False,
    )

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
    db.session.commit()


def undo_pokemon():
    db.session.execute('DELETE FROM pokemon_table')
    db.session.commit()

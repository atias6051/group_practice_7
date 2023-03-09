from ..models import db, PokemonType, Pokemon
from sqlalchemy import text

def seed_pokemon():
    pok1 = Pokemon(
        number= 1,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
        name= 'Bulbasaur',
        attack= 49,
        defense= 49,
        type= 'grass',
        moves= "tackle,vine whip",
        captured= True
    )
    pok2 = Pokemon(
        number= 2,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png',
        name= 'Ivysaur',
        attack= 62,
        defense= 63,
        type= 'grass',
        moves= "tackle,vine whip,razor leaf",
        captured= True
    )
    pok3 = Pokemon(
        number= 3,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png',
        name= 'Venusaur',
        attack= 82,
        defense= 83,
        type= 'grass',
        moves= "tackle,vine whip,razor leaf",
        captured= True
    )
    pok4 = Pokemon(
        number= 4,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png',
        name= 'Charmander',
        attack= 52,
        defense= 43,
        type= 'fire',
        moves= "scratch,ember,metal claw",
        captured= True
    )
    pok5 = Pokemon(
        number= 5,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png',
        name= 'Charmeleon',
        attack= 64,
        defense= 58,
        type= 'fire',
        moves= "scratch,ember,metal claw,flamethrower",
        captured= True
    )
    pok6 = Pokemon(
        number= 6,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png',
        name= 'Charizard',
        attack= 84,
        defense= 78,
        type= 'fire',
        moves= "flamethrower,wing attack,slash,metal claw",
        captured= True
    )
    pok7 = Pokemon(
        number = 7,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png',
        name = 'Squirtle',
        attack = 48,
        defense = 65,
        type = 'water',
        moves = "tackle,bubble,water gun",
        captured = True
    )
    pok8 = Pokemon(
        number= 8,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png',
        name= 'Wartortle',
        attack= 63,
        defense= 80,
        type= 'water',
        moves= "tackle,bubble,water gun,bite",
        captured = False
    )
    pok9 = Pokemon(
        number=9,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png',
        name="Blastoise",
        attack=83,
        defense=100,
        type="water",
        moves="hydro pump, bubble, water gun, bite",
        encounter_rate = 0.5,
        catch_rate = 0.3,
        captured=False,
    )
    pok10 = Pokemon(
        number= 10,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png',
        name= 'Caterpie',
        attack= 30,
        defense= 35,
        type= 'bug',
        moves= "tackle",
        captured = False
    )
    pok11 = Pokemon(
        number= 12,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png',
        name= 'Butterfree',
        attack= 45,
        defense= 50,
        type= 'bug',
        moves= "confusion,gust,psybeam,silver wind",
        captured= False
    )

    pok12 = Pokemon(
        number= 13,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png',
        name= 'Weedle',
        attack= 35,
        defense= 30,
        type= 'bug',
        moves= "poison sting",
        captured= False
    )
    pok13 = Pokemon(
        number= 16,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png',
        name= 'Pidgey',
        attack= 45,
        defense= 40,
        type= 'normal',
        moves= "tackle,gust",
        captured= False
    )

    pok14 = Pokemon(
        number= 17,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png',
        name= 'Pidgeotto',
        attack= 60,
        defense= 55,
        type= 'normal',
        moves= "tackle,gust,wing attack",
        captured= False
    )

    pok15 = Pokemon(
        number= 25,
        image_url= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
        name= 'Pikachu',
        attack= 55,
        defense= 40,
        type= 'electric',
        moves= "growl,electro ball,feint",
        captured= False
    )

    db.session.add_all([pok1, pok2, pok3, pok4, pok5, pok6, pok7, pok8, pok9, pok10, pok11, pok12, pok13, pok14, pok15])
    db.session.commit()

def undo_seed_pokemon():
    db.session.execute(text("DELETE FROM pokemons"))
    db.session.commit()

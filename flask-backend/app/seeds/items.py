from app.models import db, Item
from faker import Faker
from random import choice

faker = Faker()


def seed_items():
    lst = list(range(1, 11))
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
    ]
    for num in lst:
        temp = Item(
            name=faker.text(),
            price=str(choice(lst) * 2),
            happiness=str(choice(lst) * 6),
            image_url=choice(images),
            pokemonId = num
        )
        db.session.add(temp)
    db.session.commit()


def undo_items():
    db.session.execute("DELETE FROM items")
    db.session.commit()

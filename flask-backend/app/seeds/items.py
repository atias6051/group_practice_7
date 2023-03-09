from ..models import db, Item, Pokemon
from sqlalchemy import text
from random import randint

def seed_items():
    item1 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon1',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item2 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon2',
        price= randint(10, 20),
        pokemonId= randint(1,15)
    )
    item3 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon3',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item4 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon4',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item5 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon5',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item6 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon6',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item7 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon7',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item8 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon8',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item9 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon9',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item10 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon10',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item11 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon11',
        price= randint(10, 20),
        pokemonId= randint(1,15)
    )
    item12 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon12',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item13 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon13',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item14 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon14',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )
    item15 = Item(
        happiness=randint(1, 100),
        imageUrl='https://images.unsplash.com/photo-1609845768806-767fcfc317b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80.',
        name= 'pokemon15',
        price= randint(10, 20),
        pokemonId= randint(1,15),
    )

    db.session.add_all([item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15])
    db.session.commit()

def undo_items_table():
    db.session.execute("DELETE from items")
    db.session.commit()

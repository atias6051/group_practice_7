from flask import Flask, Blueprint, request, jsonify
from app.models import db, Pokemon, PokemonType, Item
from ..forms import PokeForm, ItemForm
import json


pokemon_routes = Blueprint("pokemon", __name__)

# Get All Pokemon
@pokemon_routes.route("/")
def get_pokemons():
    all_pokemon = Pokemon.query.all()
    return [pokemon.to_dict() for pokemon in all_pokemon]


# Create a Pokemon
@pokemon_routes.route("/", methods=["POST"])
def make_pokemon():
    res = request.get_json()
    pokemon_moves = res["moves"]
    my_moves = ", ".join(pokemon_moves)
    form = PokeForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    # print("back end ========= res---------------", res, my_moves)
    if form.validate_on_submit():
        pokemon = Pokemon(
            number=res["number"],
            attack=res["attack"],
            defense=res["defense"],
            image_url=res["imageUrl"],
            name=res["name"],
            type=res["type"],
            moves=my_moves,
            encounter_rate=0.5,
            catch_rate=0.3,
            captured=False,
        )
        db.session.add(pokemon)
        db.session.commit()
        return pokemon.to_dict()
    # return "Bad Data"


# Get Pokemon types
@pokemon_routes.route("/types")
def get_pokemon_types():
    data = PokemonType.query.all()
    return [type.type for type in data]


# Get items by pokemon id
@pokemon_routes.route("/<int:id>/items")
def get_items_pokemon_id(id):
    data = Pokemon.query.get(id)
    # items = [item for item in data.items]
    # print("backend ==== poke ITEMS **************=========", items)
    # return items
    return [item.to_dict() for item in data.items]


# create item by pokemon id
@pokemon_routes.route("/<int:id>/items", methods=["POST"])
def create_item(id):
    # items = [item.id for item in data.items]
    res = request.get_json()
    form = ItemForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        item = Item(
            name=res["name"],
            happiness=res["happiness"],
            price=res["price"],
            image_url="random.com",
            pokemonId=id,
        )
        db.session.add(item)
        db.session.commit()
        return item.to_dict()
    # return "Bad Data"

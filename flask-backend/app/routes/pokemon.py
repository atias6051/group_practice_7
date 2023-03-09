from flask import Flask, Blueprint
from ..models import Pokemon

bp = Blueprint("pokemon", __name__)

@bp.route('/pokemon')
def get_all_pokemons():
    return [pokemon.to_dict() for pokemon in Pokemon.query.all()]

from flask import Flask, Blueprint,request
from ..models import Pokemon
from ..form import PokemonForm
bp = Blueprint("pokemon", __name__)

@bp.route('/pokemon')
def get_all_pokemons():
    return [pokemon.to_dict() for pokemon in Pokemon.query.all()]


@bp.route('/pokemon/<int:id>')
def get_single_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()


@bp.route('/pokemon', methods=["POST"])
def create_pokemon():
    res=request.get_json()
    form=PokemonForm()
    data = form.data
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        if data['move2']:
            move = f"{data['move1']},{data['move2']}"
        else:
            move = data['move1']
        new_pokemon = Pokemon(
            number=data['number'],
            attack = data['attack'],
            defense = data['defense'],
            img_url = data['img_url'],
            type = data['type'],
            moves = move
        )
        db.session.add(new_pokemon)
        db.session.commit()
        return new_pokemon.to_dict()
    if form.errors:
        return { "errors": form.errors }

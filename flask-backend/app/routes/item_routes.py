from flask import Flask, Blueprint, request, jsonify
from app.models import db, Pokemon, PokemonType, Item
from ..forms import PokeForm, ItemForm
import json


item_routes = Blueprint("item", __name__)


# update item by pokemon id
@item_routes.route("/<int:id>", methods=["PUT"])
def edit_item(id):
    data = Item.query.get(id)
    res = request.get_json()
    if data:
        data.name = res["name"]
        data.happiness = res["happiness"]
        data.price = res["price"]
        db.session.commit()
        return data.to_dict()


# delete item
@item_routes.route("/<int:id>", methods=["DELETE"])
def delete_item(id):
    data = Item.query.get(id)
    if data:
        db.session.delete(data)
        db.session.commit()
    return {"Response": f"Successfully deleted item."}

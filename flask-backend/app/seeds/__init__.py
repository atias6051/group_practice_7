from .pokemon_type import seed_pokemon_type_table,undo_pokemon_type_table
from .pokemon import seed_pokemon, undo_seed_pokemon
from .items import seed_items, undo_items_table
from flask.cli import AppGroup

seed_commands = AppGroup("seed")

@seed_commands.command("all")
def all_seed_commands():
    seed_pokemon_type_table()
    seed_pokemon()
    seed_items()


@seed_commands.command("undo")
def all_undo_commands():
    undo_items_table()
    undo_seed_pokemon()
    undo_pokemon_type_table()

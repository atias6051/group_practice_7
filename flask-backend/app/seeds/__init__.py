from flask.cli import AppGroup
from .pokemon import seed_pokemon, undo_pokemon
from .pokemon_types import seed_pokemon_types, undo_pokemon_types
from .items import seed_items, undo_items


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    # Add other seed functions here
    seed_pokemon()
    seed_pokemon_types()
    seed_items()


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    # Add other undo functions here
    undo_pokemon()
    undo_pokemon_types()
    undo_items()

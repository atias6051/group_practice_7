# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, Blueprint
from .config import Config
from .models import db, Pokemon, Item, PokemonType
from flask_migrate import Migrate
from .seeds import seed_commands
from .routes.pokemon_routes import pokemon_routes
from .routes.item_routes import item_routes
import os


app = Flask(__name__)
app.cli.add_command(seed_commands)
app.config.from_object(Config)


# register bps here
app.register_blueprint(pokemon_routes, url_prefix="/api/pokemon")
app.register_blueprint(item_routes, url_prefix="/api/items")


db.init_app(app)
Migrate(app, db)


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        "csrf_token",
        generate_csrf(),
        secure=True if os.environ.get("FLASK_ENV") == "production" else False,
        samesite="Strict" if os.environ.get("FLASK_ENV") == "production" else None,
        httponly=True,
    )
    return response


# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, redirect
from flask_migrate import Migrate
import os
from .routes.pokemon import bp
from .config import Configuration
from .models import db
from .seeds import seed_commands
from .form import PokemonForm


app = Flask(__name__)
app.cli.add_command(seed_commands)
app.config.from_object(Configuration)
app.register_blueprint(bp, url_prefix="/api")
db.init_app(app)
Migrate(app, db)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route('/')
def index():
    return True

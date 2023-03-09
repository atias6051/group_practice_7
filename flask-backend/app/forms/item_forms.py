from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, BooleanField, FloatField, URLField
from wtforms.validators import DataRequired, URL


class ItemForm(FlaskForm):
    happiness = StringField("Happiness", validators=[DataRequired()])
    imageUrl = URLField("ImageUrl", validators=[DataRequired(), URL()])
    name = StringField("Name", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    pokemonId = IntegerField("PokemonId", validators=[DataRequired()])

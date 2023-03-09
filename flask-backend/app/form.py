from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, BooleanField, FloatField, URLField
from wtforms.validators import DataRequired, URL
from .models import PokemonType

selectChoices = list(PokemonType.query.all().type)
print("###$$$$$$$$$####", selectChoices)

class PokemonForm(FlaskForm):
    number = IntegerField("Number",validators=[DataRequired()])
    attack = IntegerField("Attack",validators=[DataRequired()])
    defence = IntegerField("Defense",validators=[DataRequired()])
    image_url = StringField("Image URL", validators=[DataRequired()])
    name = StringField("Nmae", validators=[DataRequired()])
    type = SelectField("Type",choices=selectChoices, validators=[DataRequired()])

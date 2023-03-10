from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, BooleanField, FloatField, URLField
from wtforms.validators import DataRequired, URL, NumberRange
from .models import PokemonType
# selectChoices = PokemonType.query.all()
# print("###$$$$$$$$$####", selectChoices)

class PokemonForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired(), NumberRange(min=1, message=None)])
    attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min=0, max=100)])
    defence = IntegerField("Defense", validators=[DataRequired(), NumberRange(min=0, max=100)])
    image_url = StringField("Image URL", validators=[DataRequired()])
    name = StringField("Nmae", validators=[DataRequired()])
    #type = SelectField("Type",choices=selectChoices, validators=[DataRequired()])
    type=StringField("Type")
    move1=StringField("Move1")
    move2=StringField("Move2")
    submit=SubmitField("Create New Pokemon")

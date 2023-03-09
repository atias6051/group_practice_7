from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, BooleanField, FloatField, URLField
from wtforms.validators import DataRequired, URL


class PokeForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    attack = IntegerField("Attack", validators=[DataRequired()])
    defense = IntegerField("Defense", validators=[DataRequired()])
    imageUrl = URLField("ImageUrl", validators=[DataRequired(), URL()])
    name = StringField("Name", validators=[DataRequired()])
    type = StringField("Type", validators=[DataRequired()])
    moves = StringField("Moves", validators=[DataRequired()])
    encounterRate = FloatField("Encounter Rate", validators=[DataRequired()])
    catchRate = FloatField("Catch Rate", validators=[DataRequired()])
    captured = BooleanField("Captured", validators=[DataRequired()])

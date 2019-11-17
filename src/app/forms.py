from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, FloatField, IntegerField, Label, TimeField,
                     PasswordField, SelectField, SelectMultipleField, DateTimeField,
                     StringField, SubmitField, TextAreaField, FileField)
from wtforms.validators import (URL, DataRequired, Email, EqualTo, Length,
                                NumberRange, Optional, ValidationError)


class FootballPlayers(FlaskForm):
    name = StringField(
        "Имя",
        validators=[DataRequired()],
        id="football_players_name_field"
    )
    submit = SubmitField("Показать", id="submit_button")

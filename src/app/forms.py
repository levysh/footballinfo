from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, FloatField, IntegerField, Label, TimeField,
                     PasswordField, SelectField, SelectMultipleField, DateTimeField,
                     StringField, SubmitField, TextAreaField, FileField)
from wtforms.validators import (URL, DataRequired, Email, EqualTo, Length,
                                NumberRange, Optional, ValidationError)


class FootballPlayers(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class TopTeamsByPlayersAmount(FlaskForm):
    count = IntegerField(
        "Количество топ-команд",
        default=10,
        id="top_teams_by_players_amount_count"
    )
    submit = SubmitField("Показать", id="submit_button")


class TeamWinsCount(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class PlayersMatches(FlaskForm):
    count = IntegerField(
        "Количество топ-игроков",
        default=10,
        id="player_matches_count"
    )
    submit = SubmitField("Показать", id="submit_button")


class GoalsInLeagues(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class TeamGoalsCount(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class CountryMeanPlayerStats(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class TopHighestPlayers(FlaskForm):
    count = IntegerField(
        "Количество топ-игроков",
        default=10,
        id="top_highest_players_count"
    )
    submit = SubmitField("Показать", id="submit_button")


class YoungestPlayersInLeague(FlaskForm):
    league_id = IntegerField(
        "ID лиги",
        default=17642,
        id="youngest_players_in_league_league_id"
    )
    count = IntegerField(
        "Количество самых молодых игроков",
        default=10,
        id="youngest_players_in_league_count"
    )
    submit = SubmitField("Показать", id="sumbit_button")


class LeaguePlayersMatchesRatio(FlaskForm):
    league_id = IntegerField(
        "ID лиги",
        default=17642,
        id="league_players_matches_ratio_league_id"
    )
    submit = SubmitField("Показать", id="sumbit_button")


class TeamScoredAndMissedGoals(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class LeagueTeamsGoalsGap(FlaskForm):
    league_id = IntegerField(
        "ID лиги",
        default=17642,
        id="league_teams_goals_gap_league_id"
    )
    submit = SubmitField("Показать", id="submit_button")


class TeamRatingByWins(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class LeagueHeaviestPlayers(FlaskForm):
    league_id = IntegerField(
        "ID лиги",
        default=17642,
        id="league_heaviest_players_league_id"
    )
    submit = SubmitField("Показать", id="submit_button")


class LeagueLastMatches(FlaskForm):
    league_id = IntegerField(
        "ID лиги",
        default=17642,
        id="league_last_matches_league_id"
    )
    count = IntegerField(
        "Количество последних матчей",
        default=10,
        id="league_last_matches_count"
    )
    submit = SubmitField("Показать", id="submit_button")


class LeagueHomeGoalsStat(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class LeagueMedianSumGoals(FlaskForm):
    submit = SubmitField("Показать", id="submit_button")


class ViewTeamsPerCountry(FlaskForm):
    select = SelectField("Показать всю VIEW или SELECT", choices=[('view', 'VIEW'), ('select', "SELECT")])
    submit = SubmitField("Показать", id="submit_button")


class ViewPlayersLastStatistic(FlaskForm):
    select = SelectField("Показать всю VIEW или SELECT", choices=[('view', 'VIEW'), ('select', "SELECT")])
    rating = IntegerField(
        "Минимальный рейтинг игрока",
        default=85,
    )
    submit = SubmitField("Показать", id="submit_button")


class ViewMatchesWithTeamNames(FlaskForm):
    select = SelectField("Показать всю VIEW или SELECT", choices=[('view', 'VIEW'), ('select', "SELECT")])
    team = StringField(
        "Команда",
        default='FC Barcelona',
    )
    submit = SubmitField("Показать", id="submit_button")


class ViewAverageMatchPlayersRating(FlaskForm):
    select = SelectField("Показать всю VIEW или SELECT", choices=[('view', 'VIEW'), ('select', "SELECT")])
    rating = IntegerField(
        "Минимальный средний рейтинг игроков матча",
        default=82,
    )
    submit = SubmitField("Показать", id="submit_button")


class ViewPlayersLifeAttributes(FlaskForm):
    select = SelectField("Показать VIEW, сделать UPDATE или показать исходную таблицу",
                         choices=[('view', 'VIEW'), ('update', "UPDATE"), ("initial", "INITIAL")])
    height = IntegerField(
        "Рост (минимальный по которому будет создана VIEW или значение на которое перезаписать в UPDATE)",
        default=190,
    )
    weight = IntegerField(
        "Максимальный вес (в кг)",
        default=75,
    )
    name = StringField(
        "Имя игрока",
        default='Aaron Wilbraham',
    )

    submit = SubmitField("Показать", id="submit_button")


class CreateNewPlayer(FlaskForm):
    name = StringField(
        'Имя игрока'
    )
    birthday = StringField(
        'Дата рождения',
        default='2012-01-01', description='в формате YYYY-MM-DD'
    )
    weight = FloatField(
        'Вес игрока'
    )
    height = FloatField(
        'Рост игрока'
    )

    submit = SubmitField('Добавить', id='add_button')
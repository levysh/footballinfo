import os

from src.app.forms import (  # in order of adding
    FootballPlayers,
    TopTeamsByPlayersAmount,
    TeamWinsCount,
    PlayersMatches,
    GoalsInLeagues,
    TeamGoalsCount,
    CountryMeanPlayerStats,
    TopHighestPlayers,
    YoungestPlayersInLeague,
    LeaguePlayersMatchesRatio,
    TeamScoredAndMissedGoals,
    LeagueTeamsGoalsGap,
    TeamRatingByWins,
    LeagueHeaviestPlayers,
    LeagueLastMatches,
    LeagueHomeGoalsStat,
    LeagueMedianSumGoals
)
from src.app.routes.queries import bp
from src.app import db

from flask import redirect, url_for, render_template, current_app
from sqlalchemy import text


def generate_table_from_query(query_name, query_args):
    with open(os.path.join(current_app.config['QUERIES_PATH'], query_name)) as f:
        sql = text(f.read().format(**query_args))
    result = db.engine.execute(sql)
    columns = []
    values = [[]]
    for rowproxy in result:
        columns = [column for column, _ in rowproxy.items()]
        values.append([value for _, value in rowproxy.items()])
    values[0] = columns
    return values


@bp.route("/ping")
def ping():
    return "OK"


@bp.route("/test", methods=["GET"])
def test():
    table = [['a', 'b', 'c'], [0, 0, 0], [0, 0, 0]]
    return render_template(
        "table.html",
        title="Футболисты",
        table=table
    )


@bp.route("/players", methods=["GET", "POST"])
def players():
    form = FootballPlayers()
    if form.validate_on_submit():
        print(form.data)
        return render_template(
            "table.html",
            title="Футболисты",
            table=generate_table_from_query('players.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Футболисты",
        form=form
    )


@bp.route("/query_1", methods=["GET", "POST"])
def query_1():
    form = FootballPlayers()
    if form.validate_on_submit():
        return "ok"
    return render_template(
        "input_form.html",
        title="Запрос 1",
        form=form
    )


@bp.route("/query_2", methods=["GET", "POST"])
def query_2():
    form = FootballPlayers()
    if form.validate_on_submit():
        return "ok"
    return render_template(
        "input_form.html",
        title="Запрос 2",
        form=form
    )


@bp.route("/top_teams_by_players_amount", methods=["GET", "POST"])
def top_teams_by_players_amount():
    form = TopTeamsByPlayersAmount()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Топ команд по количеству игроков",
            table=generate_table_from_query('top_teams_by_players_amount.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Топ команд по количеству игроков",
        form=form
    )


@bp.route("/team_wins_count", methods=["GET", "POST"])
def team_wins_count():
    form = TeamWinsCount()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Количество побед каждой из команд",
            table=generate_table_from_query('team_wins_count.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Количество побед каждой из команд",
        form=form
    )


@bp.route("/players_matches", methods=["GET", "POST"])
def players_matches():
    form = PlayersMatches()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Топ игроков по количеству сыгранных матчей",
            table=generate_table_from_query('players_matches.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Топ игроков по количеству сыгранных матчей",
        form=form
    )


@bp.route("/goals_in_leagues", methods=["GET", "POST"])
def goals_in_leagues():
    form = GoalsInLeagues()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Количество забитых мячей в каждой лиге",
            table=generate_table_from_query('goals_in_leagues.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Количество забитых мячей в каждой лиге",
        form=form
    )


@bp.route("/team_goals_count", methods=["GET", "POST"])
def team_goals_count():
    form = TeamGoalsCount()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Количество забитых мячей каждой из команд",
            table=generate_table_from_query('team_goals_count.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Количество забитых мячей каждой из команд",
        form=form
    )


@bp.route("/country_mean_player_stats", methods=["GET", "POST"])
def country_mean_player_stats():
    form = CountryMeanPlayerStats()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Средний рост/вес/возраст игроков в странах",
            table=generate_table_from_query('country_mean_player_stats.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Средний рост/вес/возраст игроков в странах",
        form=form
    )


@bp.route("/top_highest_players", methods=["GET", "POST"])
def top_highest_players():
    form = TopHighestPlayers()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Топ самых высоких игроков",
            table=generate_table_from_query('top_highest_players.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Топ самых высоких игроков",
        form=form
    )


@bp.route("/youngest_players_in_league", methods=["GET", "POST"])
def youngest_players_in_league():
    form = YoungestPlayersInLeague()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Самые молодые игроки лиги",
            table=generate_table_from_query('youngest_players_in_league.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Самые молодые игроки лиги",
        form=form
    )


@bp.route("/league_players_matches_ratio", methods=["GET", "POST"])
def league_players_matches_ratio():
    form = LeaguePlayersMatchesRatio()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Доля сыгранных матчей игроками в данной лиге среди всех матчей игрока",
            table=generate_table_from_query('league_players_matches_ratio.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Доля сыгранных матчей игроками в данной лиге среди всех матчей игрока",
        form=form
    )


@bp.route("/team_scored_and_missed_goals", methods=["GET", "POST"])
def team_scored_and_missed_goals():
    form = TeamScoredAndMissedGoals()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Количество забитых и пропущенных голов каждой из команд",
            table=generate_table_from_query('team_scored_and_missed_goals.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Количество забитых и пропущенных голов каждой из команд",
        form=form
    )


@bp.route("/league_teams_goals_gap", methods=["GET", "POST"])
def league_teams_goals_gap():
    form = LeagueTeamsGoalsGap()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Отставание в забитых голах для всех команд лиги",
            table=generate_table_from_query('league_teams_goals_gap.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Отставание в забитых голах для всех команд лиги",
        form=form
    )


@bp.route("/team_rating_by_wins", methods=["GET", "POST"])
def team_rating_by_wins():
    form = TeamRatingByWins()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Рейтинг команд по числу побед",
            table=generate_table_from_query('team_rating_by_wins.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Рейтинг команд по числу побед",
        form=form
    )


@bp.route("/league_heaviest_players", methods=["GET", "POST"])
def league_heaviest_players():
    form = LeagueHeaviestPlayers()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Рейтинг самых тяжёлых игроков лиги",
            table=generate_table_from_query('league_heaviest_players.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Рейтинг самых тяжёлых игроков лиги",
        form=form
    )


@bp.route("/league_last_matches", methods=["GET", "POST"])
def league_last_matches():
    form = LeagueLastMatches()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Последние игры лиги",
            table=generate_table_from_query('league_last_matches.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Последние игры лиги",
        form=form
    )


@bp.route("/league_home_goals_stat", methods=["GET", "POST"])
def league_home_goals_stat():
    form = LeagueHomeGoalsStat()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Статистика количества забитых голов домашней командой",
            table=generate_table_from_query('league_home_goals_stat.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Статистика количества забитых голов домашней командой",
        form=form
    )


@bp.route("/league_median_sum_goals", methods=["GET", "POST"])
def league_median_sum_goals():
    form = LeagueMedianSumGoals()
    if form.validate_on_submit():
        return render_template(
            "table.html",
            title="Медианное количество забитых голов в матчах каждой из лиг",
            table=generate_table_from_query('league_median_sum_goals.sql', form.data)
        )
    return render_template(
        "input_form.html",
        title="Медианное количество забитых голов в матчах каждой из лиг",
        form=form
    )


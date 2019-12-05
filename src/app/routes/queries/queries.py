import os
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    LeagueMedianSumGoals,
    ViewTeamsPerCountry,
    ViewPlayersLastStatistic,
    ViewMatchesWithTeamNames,
    ViewAverageMatchPlayersRating,
    ViewPlayersLifeAttributes
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


def generate_new_graph(values):
    mpl.use('agg')
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 54000, 0, 150])

    plt.title('Статистика голов')
    plt.xlabel('Команды')
    plt.ylabel('Голы')

    plt.hist([int(row[1]) for row in values[1:]])

    plt.legend(loc = 'upper right')
    fig.savefig(os.path.join(current_app.config['IMAGES_PATH'], 'graph.png'))
    return "ok"


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
        values = generate_table_from_query('team_scored_and_missed_goals.sql', form.data)
        generate_new_graph(values)
        return render_template(
            "table.html",
            title="Количество забитых и пропущенных голов каждой из команд",
            table=generate_table_from_query('team_scored_and_missed_goals.sql', form.data),
            show_graph=True
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

@bp.route("/view_teams_per_country", methods=["GET", "POST"])
def view_teams_per_country():
    form = ViewTeamsPerCountry()
    if form.validate_on_submit():
        show_view_only = True if form.data['select'] == 'view' else False
        sql_path ='view_teams_per_country.sql' if show_view_only else "view_s_teams_per_country.sql"
        title = '(VIEW) команды по странам и лигам' if show_view_only else 'Количество команд в каждой лиге'
        return render_template(
            "table.html",
            title=title,
            table=generate_table_from_query(sql_path, form.data)
        )
    return render_template(
        "input_form.html",
        title="Количество команд в каждой лиге",
        form=form
    )

@bp.route("/view_players_last_statistic", methods=["GET", "POST"])
def view_players_last_statistic():
    form = ViewPlayersLastStatistic()
    if form.validate_on_submit():
        show_view_only = True if form.data['select'] == 'view' else False
        sql_path ='view_players_last_statistic.sql' if show_view_only else "view_s_players_last_statistic.sql"
        title = '(VIEW) Основная статистика по игрокам' if show_view_only else 'Статистика по самым топовым игрокам'
        return render_template(
            "table.html",
            title=title,
            table=generate_table_from_query(sql_path, form.data)
        )
    return render_template(
        "input_form.html",
        title="Основная статистика по игрокам",
        form=form
    )

@bp.route("/view_matches_with_team_names", methods=["GET", "POST"])
def view_matches_with_team_names():
    form = ViewMatchesWithTeamNames()
    if form.validate_on_submit():
        show_view_only = True if form.data['select'] == 'view' else False
        sql_path ='view_matches_with_team_names.sql' if show_view_only else "view_s_matches_with_team_names.sql"
        title = '(VIEW) Сыгранные матчи' if show_view_only else 'Информация по нужной команде'
        return render_template(
            "table.html",
            title=title,
            table=generate_table_from_query(sql_path, form.data)
        )
    return render_template(
        "input_form.html",
        title="Сыгранные матчи с результатом",
        form=form
    )

@bp.route("/view_average_match_players_rating", methods=["GET", "POST"])
def view_average_match_players_rating():
    form = ViewAverageMatchPlayersRating()
    if form.validate_on_submit():
        show_view_only = True if form.data['select'] == 'view' else False
        sql_path ='view_average_match_players_rating.sql' if show_view_only else "view_s_average_match_players_rating.sql"
        title = '(VIEW) Средний рейтинг по матчам' if show_view_only else 'Матчи с наибольшим рейтингом'
        return render_template(
            "table.html",
            title=title,
            table=generate_table_from_query(sql_path, form.data)
        )
    return render_template(
        "input_form.html",
        title="Средний рейтинг по матчам",
        form=form
    )

@bp.route("/view_players_life_attributes", methods=["GET", "POST"])
def view_players_life_attributes():
    form = ViewPlayersLifeAttributes()
    if form.validate_on_submit():
        if form.data['select'] == 'view':
            return render_template(
                "table.html",
                title='(VIEW) Статистика игроков',
                table=generate_table_from_query("view_players_life_attributes.sql", form.data)
            )
        elif form.data['select'] == 'update':
            return render_template(
                "table.html",
                title='Попробовали обновить данные по запросу в VIEW',
                table=generate_table_from_query("view_update_players_life_attributes.sql", form.data)
            )
        elif form.data['select'] == 'initial':
            return render_template(
                "table.html",
                title='Исходная таблица по которой была построена VIEW',
                table=generate_table_from_query("view_s_init_players_life_attributes.sql", form.data)
            )
    return render_template(
        "input_form.html",
        title="Средний рейтинг по матчам",
        form=form
    )

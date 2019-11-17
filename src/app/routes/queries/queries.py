import os

from src.app.forms import FootballPlayers
from src.app.routes.queries import bp
from src.app import db

from flask import redirect, url_for, render_template, current_app
from sqlalchemy import text


def generate_table_from_query(query_name):
    with open(os.path.join(current_app.config['QUERIES_PATH'], query_name)) as f:
        sql = text(f.read())
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
        return render_template(
            "table.html",
            title="Футболисты",
            table=generate_table_from_query('players.sql')
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

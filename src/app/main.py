from flask import Blueprint
from flask import redirect, url_for, render_template
from app.forms import FootballPlayers
from app import db


bp = Blueprint("main", __name__)


@bp.route("/favicon.ico")
def favicon():
    return redirect(url_for('static', filename='ball.ico'))


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/ping")
def ping():
    return "OK"


@bp.route("/form", methods=["GET", "POST"])
def form():
    form = FootballPlayers()
    if form.validate_on_submit():
        return "ok"
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

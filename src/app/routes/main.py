from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint("main", __name__)


@bp.route("/favicon.ico")
def favicon():
    return redirect(url_for('static', filename='ball.ico'))


@bp.route("/")
def index():
    return render_template("index.html")

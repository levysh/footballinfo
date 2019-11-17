from flask import Blueprint

bp = Blueprint("queries", __name__)

from src.app.routes.queries import queries
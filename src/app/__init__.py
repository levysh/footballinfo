import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from src.app.config import Config

BASE_DIR = os.path.dirname(__file__)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    app.config['QUERIES_PATH'] = os.path.join(BASE_DIR, 'queries')

    from src.app.routes import queries_bp, main_bp
    app.register_blueprint(queries_bp)
    app.register_blueprint(main_bp)

    db.init_app(app)
    Bootstrap(app)
    return app

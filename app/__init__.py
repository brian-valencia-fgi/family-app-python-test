import os

from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    init_db(app)
    return app


def register_blueprints(app: Flask):
    from app.routes.main import main_blueprint
    from app.routes.profile import profile_blueprint
    from app.scripts.commands import commands_blueprint

    api_blueprint = Blueprint("api", __name__)
    api_blueprint.register_blueprint(main_blueprint)
    api_blueprint.register_blueprint(profile_blueprint, url_prefix="/profiles")

    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.register_blueprint(commands_blueprint)


def init_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

    migrate = Migrate(compare_type=True)

    db.init_app(app)
    migrate.init_app(app, db)

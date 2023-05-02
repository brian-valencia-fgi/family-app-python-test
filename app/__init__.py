import os
from http import HTTPStatus
from typing import Dict, List, Union

from flask import Blueprint, Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    register_error_handlers(app)
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


def register_error_handlers(app: Flask):
    from marshmallow import ValidationError

    from app.errors import ResourceNotFoundError

    @app.errorhandler(ResourceNotFoundError)
    def handle_not_found(e: ResourceNotFoundError):
        return _get_error_json("NOT FOUND", e.description, HTTPStatus.NOT_FOUND)

    @app.errorhandler(ValidationError)
    def handle_invalid_schemas(e: ValidationError):
        return _get_error_json("BAD REQUEST", e.messages, HTTPStatus.BAD_REQUEST)


def _get_error_json(message: str, description: Union[str, List, Dict] = "", status_code: Union[int, HTTPStatus] = HTTPStatus.INTERNAL_SERVER_ERROR):
    return jsonify({
        "error": message,
        "description": description
    }), status_code

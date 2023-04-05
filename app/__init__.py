from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    from app.routes.main import main_blueprint
    from app.routes.profile import profile_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(profile_blueprint, url_prefix="/profiles")

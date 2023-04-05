from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    from app.routes.main import main_blueprint
    from app.routes.profile import profile_blueprint

    api_blueprint = Blueprint("api", __name__)
    api_blueprint.register_blueprint(main_blueprint)
    api_blueprint.register_blueprint(profile_blueprint, url_prefix="/profiles")
    
    app.register_blueprint(api_blueprint, url_prefix="/api")

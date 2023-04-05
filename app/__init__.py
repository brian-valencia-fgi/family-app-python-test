from flask import Flask
from http import HTTPStatus


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        {
            "message": "API is working fine!"
        }, HTTPStatus.OK

    @app.route("/profiles/<profile_id>")
    def get_profile(profile_id):
        return {
            "message": f"get profile number {profile_id}"
        }, HTTPStatus.OK

    @app.route('/profiles/')
    def get_profiles():
        return {
            "message": "get profiles list"
        }, HTTPStatus.OK

    return app

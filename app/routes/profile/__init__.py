from . import views
from flask import Blueprint
from flask_restful import Api

profile_blueprint = Blueprint("profile", __name__)
api = Api(profile_blueprint)

api.add_resource(views.ProfilesApi, "/")
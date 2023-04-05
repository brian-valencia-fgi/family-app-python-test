from . import views
from flask import Blueprint
from flask_restful import Api

main_blueprint = Blueprint("main", __name__)
api = Api(main_blueprint)

api.add_resource(views.MainApi, "/")

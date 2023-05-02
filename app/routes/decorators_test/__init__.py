from flask_restful import Api
from .views import BeforeDecoratorsTestApi
from flask import Blueprint

decorators_test_blueprint = Blueprint('decorator_test_blueprint', __name__)
api = Api(decorators_test_blueprint)

api.add_resource(BeforeDecoratorsTestApi, "/") 

from flask import Blueprint
from flask_restful import Api

from .views import AfterDecoratorsTestApi, BeforeDecoratorsTestApi

decorators_test_blueprint = Blueprint('decorator_test_blueprint', __name__)
api = Api(decorators_test_blueprint)

api.add_resource(AfterDecoratorsTestApi, "/after")
api.add_resource(BeforeDecoratorsTestApi, "/before")

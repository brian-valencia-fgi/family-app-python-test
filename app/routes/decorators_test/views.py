from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from app.core import decorators_test as decorators_test_core


class BeforeDecoratorsTestApi(Resource, MethodResource):
    def post(self):
        body = request.get_json()
        response = decorators_test_core.do_stuff(body['a'], body['b'], body['c'])
        return response # what does response look like?

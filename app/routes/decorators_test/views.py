from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from app.core import decorators_test as decorators_test_core
from app.utils.decorators import request_deserializer, response_serializer
from app.schemas.decorators_test import DecoratorsTestApiSchemas


class BeforeDecoratorsTestApi(Resource, MethodResource):
    def post(self):
        body = request.get_json()
        response = decorators_test_core.do_stuff(body['a'], body['b'], body['c'])
        return response # what does response look like?

class AfterDecoratorsTestApi(Resource, MethodResource):
    @request_deserializer(DecoratorsTestApiSchemas.PostRequest)
    @response_serializer(DecoratorsTestApiSchemas.PostResponse)
    def post(self, payload: DecoratorsTestApiSchemas.PostRequest):
        return decorators_test_core.do_stuff_with_models(payload)

from flask import request
from flask_apispec import MethodResource
from flask_restful import Resource
from app.core import decorators_test as decorators_test_core
from app.utils.decorators import request_deserializer, response_serializer
from app.schemas.decorators_test import DecoratorsTestApiSchemas, DecoratorsTestPostRequest, DecoratorsTestPostResponse


class BeforeDecoratorsTestApi(Resource, MethodResource):
    # Use doc decorator here...
    # @doc(...)
    def post(self):
        body = request.get_json()
        # Will throw a ValidationError if any
        processed_body = DecoratorsTestPostRequest().load(body)
        
        # what are DecoratorsTestPostRequest's params again?...
        # no autocomplete :(
        response = decorators_test_core.do_stuff(
            processed_body['a'], processed_body['b'], processed_body['c'])
        
        # dump the response as you return it
        return DecoratorsTestPostResponse().dump(response)


class AfterDecoratorsTestApi(Resource, MethodResource):
    # these two will eventually also add docs!
    @request_deserializer(DecoratorsTestApiSchemas.PostRequest)
    @response_serializer(DecoratorsTestApiSchemas.PostResponse)
    # processed payload injected into the function's params by the request deserializer!
    def post(self, payload: DecoratorsTestApiSchemas.PostRequest):
        # function has autocomplete! lets you know it expects a DecoratorsTestApiSchemas.PostRequest
        # view the definition for it or rely on autocomplete to give hints for available fields
        
        # automatically dumped by the decorator!
        return decorators_test_core.do_stuff_with_models(payload)

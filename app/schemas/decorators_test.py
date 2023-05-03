from dataclasses import dataclass
from marshmallow import fields, Schema


# Schemas used by the Resource AFTER applying the decorators
class DecoratorsTestApiSchemas:
    @dataclass
    class PostRequest:
        a: int
        b: str
        c: float

    @dataclass
    class PostResponse:
        message: str
        body: 'DecoratorsTestApiSchemas.PostRequest'


# Schemas used by the Resource BEFORE applying the decorators
class DecoratorsTestPostRequest(Schema):
    a = fields.Int(required=True)
    b = fields.Str(required=True)
    c = fields.Float(required=True)


class DecoratorsTestPostResponse(Schema):
    message = fields.Str(required=True)
    body = fields.Nested(DecoratorsTestPostRequest())

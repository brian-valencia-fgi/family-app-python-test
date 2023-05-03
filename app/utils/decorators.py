import desert
from functools import wraps
from http import HTTPStatus
from flask import request
from typing import Callable, ClassVar, Dict, Type
import marshmallow as ma


class DataClass:
    __dataclass_fields__: ClassVar[Dict]


def request_deserializer(Model: Type[DataClass], many=False, meta: Dict = {}):
    def decorator(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            body = request.get_json()
            Schema = desert.schema_class(Model, meta=meta)
            payload = Schema(many=many).load(body)
            _add_request_doc(fn, Schema, many=many, meta=meta)
            return fn(*args, payload=payload, **kwargs)
        return wrapper
    return decorator


def response_serializer(Model: Type[DataClass], many=False, meta: Dict = {}, status_code=HTTPStatus.OK):
    def decorator(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            Schema = desert.schema_class(Model, meta=meta)
            _add_response_doc(fn, Schema, many=many, meta=meta)
            response = Schema(many=many).dump(result)
            return response, status_code
        return wrapper
    return decorator


def _add_request_doc(fn: Callable, Schema: ma.Schema, many=False, meta: Dict = {}):
    pass


def _add_response_doc(fn: Callable, Schema: ma.Schema, many=False, meta: Dict = {}):
    pass

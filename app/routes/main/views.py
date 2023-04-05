from flask_restful import Resource
from http import HTTPStatus


class MainApi(Resource):
    def get(self):
        return {"message": "API is working fine!"}, HTTPStatus.OK

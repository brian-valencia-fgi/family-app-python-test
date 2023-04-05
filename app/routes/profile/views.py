from flask_restful import Resource
from http import HTTPStatus


class ProfilesApi(Resource):
    def get(self):
        return {"message": "profile list"}, HTTPStatus.OK

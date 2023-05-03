from http import HTTPStatus

from flask import request
from flask_restful import Resource
from app.models.profile import Profile


class ProfilesApi(Resource):
    def get(self):
        return {"message": "profile list"}, HTTPStatus.OK

    def post(self):
        body = request.get_json()
        return {"message": "requested to profiles API", "body": body}, HTTPStatus.OK


class ProfileApi(Resource):
    def get(self, profile_id):
        return {"message": f"Fetching profile id {profile_id}"}, HTTPStatus.OK

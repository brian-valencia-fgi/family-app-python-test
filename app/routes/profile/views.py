from flask_restful import Resource
from http import HTTPStatus


class ProfilesApi(Resource):
    def get(self):
        return {"message": "profile list"}, HTTPStatus.OK

class ProfileApi(Resource):
    def get(self, profile_id):
        return {"message": f"Fetching profile id {profile_id}"}, HTTPStatus.OK

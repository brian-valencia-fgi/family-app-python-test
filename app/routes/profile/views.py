from http import HTTPStatus

from app import db
from flask import request
from flask_restful import Resource
from app.models.profile import Profile, ProfileSchema
from app.models.badge import BadgeSchema


class ProfilesApi(Resource):
    def get(self):
        return {"message": "profile list"}, HTTPStatus.OK

    def post(self):
        body = request.get_json()
        profile = ProfileSchema().load(body)
        badges = body.get('badges')
        badges = BadgeSchema(many=True).load(badges)
        db.session.add(profile)
        for badge in badges:
            db.session.add(badge)
        
        db.session.commit()
        return {"message": "requested to profiles API", "profile": profile, "badges": badges}, HTTPStatus.OK


class ProfileApi(Resource):
    def get(self, profile_id):
        return {"message": f"Fetching profile id {profile_id}"}, HTTPStatus.OK

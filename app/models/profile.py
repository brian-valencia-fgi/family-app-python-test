from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from dataclasses import dataclass
from datetime import datetime
from app import db
from typing import Optional
from app.models.badge_profile import BadgeProfile
from app.models.badge import Badge

from app.models.role import Role
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import EXCLUDE


class Profile(db.Model):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), server_default='1')
    role = db.relationship(Role, back_populates="users_in_role")

    name = Column(String)
    email = Column(String)
    position = Column(String)
    department = Column(String)
    image_name = Column(String)

    date_hired = Column(DateTime)
    birthdate = Column(DateTime)
    date_added = Column(DateTime, server_default=func.now())
    date_updated = Column(DateTime, server_default=func.now())
    
    badges = db.relationship(Badge, secondary=BadgeProfile.__table__)

class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Profile
        unknown=EXCLUDE

class ProfileApiPayloads:
    @dataclass
    class PostRequest:
        role_id: int
        name: str
        email: str
        position: str
        department: str
        birthdate: datetime
        date_hired: Optional[datetime] = None
        image_name: Optional[str] = None
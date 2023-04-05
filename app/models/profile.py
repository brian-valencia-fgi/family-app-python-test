from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

from app import db
from app.models.role import Role


class Profile(db.Model):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = db.relationship(Role, back_populates="users_in_role")

    name = Column(String)
    email = Column(String)
    position = Column(String)
    department = Column(String)
    image_name = Column(String)

    date_hired = Column(DateTime)
    birthdate = Column(DateTime)
    date_added = Column(DateTime)

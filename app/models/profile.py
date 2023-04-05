from sqlalchemy import Column, DateTime, Integer, String

from app import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer)

    name = Column(String)
    email = Column(String)
    position = Column(String)
    department = Column(String)
    image_name = Column(String)

    date_hired = Column(DateTime)
    birthdate = Column(DateTime)
    date_added = Column(DateTime)

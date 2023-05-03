from sqlalchemy import Boolean, Column, Integer, String

from app import db


class Badge(db.Model):
    __tablename__ = 'badges'
    id = Column(Integer, primary_key=True)
    badge_name = Column(String)
    badge_icon = Column(String)
    is_active = Column(Boolean)
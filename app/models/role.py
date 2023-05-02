from sqlalchemy import Column, DateTime, Integer, String, func

from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    role_name = Column(String)
    date_added = Column(DateTime, server_default=func.now())
    date_updated = Column(DateTime, server_default=func.now())
    users_in_role = db.relationship('Profile', back_populates='role')
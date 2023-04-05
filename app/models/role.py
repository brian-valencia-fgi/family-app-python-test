from app import db
from sqlalchemy import Column, Integer, String, DateTime

class Role(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    role_name = Column(String)
    date_added = Column(DateTime)
    users_in_role = db.relationship('Profile', back_populates='role')
from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app import db


class BadgeProfile(db.Model):
    __tablename__ = 'badge_profiles'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id', ondelete='CASCADE'))
    badge_id = Column(Integer, ForeignKey('badges.id', ondelete='CASCADE'))
    date_added = Column(DateTime)
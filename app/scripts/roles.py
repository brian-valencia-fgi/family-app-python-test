from app.models.role import Role
from app import db


def seed_roles_helper():
    roles = [
        Role(role_name="user"),
        Role(role_name="admin"),
        Role(role_name="super-admin")
    ]
    for role in roles:
        db.session.merge(role)

    db.session.commit()

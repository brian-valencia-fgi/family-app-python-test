from app.models.role import Role
from app import db


def seed_roles_helper():
    roles = [
        Role(id=1, role_name="user"),
        Role(id=2, role_name="admin"),
        Role(id=3, role_name="super-admin"),
        Role(role_name="super-super-admin")
    ]
    for role in roles:
        print("Adding role", role.role_name)
        db.session.merge(role)

    db.session.commit()

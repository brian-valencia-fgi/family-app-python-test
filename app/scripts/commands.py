from app.scripts import commands_blueprint
from app.scripts.roles import seed_roles_helper

@commands_blueprint.cli.command('seed-roles')
def seed_roles():
    seed_roles_helper()
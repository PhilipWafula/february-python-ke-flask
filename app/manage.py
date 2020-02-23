from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
import os

# TODO: Make this DRY
parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_directory)
sys.path.append(os.getcwd())

from app.server import create_app, db
from app.server.models import import_models

import_models()
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_dir)
sys.path.append(os.getcwd())

from server import create_app, db

app = create_app()
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

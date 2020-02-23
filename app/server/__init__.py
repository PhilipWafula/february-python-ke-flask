import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


def create_app():
    # create and configure application
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)


db = SQLAlchemy(session_options={
    "expire_on_commit": not config.IS_TEST,
    # enable_baked_queries prevents the before_compile query from getting trapped.
    # Shouldn't by default but ¯\_(ツ)_/¯
    # https://docs.sqlalchemy.org/en/13/orm/extensions/baked.html
    "enable_baked_queries": False,
})


def register_blueprints(app):
    versioned_api_url = '/api/v1'

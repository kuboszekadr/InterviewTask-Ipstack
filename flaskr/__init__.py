from configparser import ConfigParser

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    from .api import api, user
    from dbModel import db
    app.register_blueprint(api.bp)
    app.register_blueprint(user.bp)

    config = ConfigParser()
    config.read(r'.\config.ini')

    app.config['SECRET_KEY'] = config['SECRET']['secret_key']
    app.config['IPSTACK_FIELDS'] = eval(config['DATA']['fields'])

    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['uri']
    app.config['JWT'] = config['JWT']['secret_key']

    db.init_app(app)
    jwt.init_app(app)
    
    return app

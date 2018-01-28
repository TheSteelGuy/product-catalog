#myapp/__init__.py
#coding:"utf-8"
import os
#third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#local imports 

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__,instance_path=os.path.join(os.path.abspath(os.curdir),'instance'), instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('myconfig.py')
    db.init_app(app)
    
    migrate = Migrate(app,db)
    
    #register Blueprints
    from catalog import catalog as catalog_blueprint
    app.register_blueprint(catalog_blueprint)
    return app








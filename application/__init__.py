from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #Initialization
    db.init_app(app)

    #Blueprint registration
    from .api import api as api_bp
    app.register_blueprint(api_bp,url_prefix="/api/v1")
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    from .api import api_login as api_login_bp
    app.register_blueprint(api_login_bp,url_prefix="/api/v1")

    return app
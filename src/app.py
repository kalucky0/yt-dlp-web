import os
from flask import Flask

from .config import config
from .routes.main import main_bp
from .routes.download import download_bp
from .routes.api import api_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__, template_folder='templates')
    
    app_config = config[config_name]
    app.config.from_object(app_config)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(download_bp)
    app.register_blueprint(api_bp)
    
    return app

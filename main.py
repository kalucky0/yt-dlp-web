import os
from src.app import create_app
from src.config import config

if __name__ == '__main__':
    config_name = os.environ.get('FLASK_ENV', 'development')
    app = create_app(config_name)
    
    app_config = config[config_name]
    
    app.run(
        debug=app_config.DEBUG,
        host=app_config.HOST,
        port=app_config.PORT
    )

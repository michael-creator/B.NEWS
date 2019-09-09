from flask import Flask
from flask_boostrap import bootstrap
from config import config_options

# Initializing application
app = Flask(__name__,instance_relative_config = True)

#setting up configuration
app.config.from_object(DevConfig)

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

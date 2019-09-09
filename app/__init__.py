from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)


def create_app(config_name):

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.config.from_object(config_options[config_name])
    # setting config
    # from .request import configure_request
    # configure_request(app)
    bootstrap.init_app(app)
    return app

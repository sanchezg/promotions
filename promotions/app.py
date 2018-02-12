import logging

from flask import Flask, Blueprint
from promotions import settings
from promotions.sales.views import ns
from promotions.api.restplus import api
from promotions.database import db

app = Flask(__name__)
log = logging.getLogger(__name__)


def configure_app(flask_app, config_name='devel'):
    flask_app.config.from_object(settings.app_config.get(config_name))


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(ns)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()

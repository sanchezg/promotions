class Config(object):
    DEBUG = False
    TESTING = False
    # Flask settings
    FLASK_SERVER_NAME = 'localhost:8888'

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    FLASK_DEBUG = True  # Do not use debug mode in production
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


app_config = {
    'prod': ProductionConfig,
    'devel': DevelopmentConfig,
    'test': TestingConfig
}

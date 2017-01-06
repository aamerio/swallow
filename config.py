# pylint: disable=missing-docstring

class BaseConfig(object):
    PATH_SUFFIX = "/api"
    DB = 'db'
    VERSION = '0.0.1'
    ENABLED_MODULES = (
        'mongodb',
    )

class ProductionConfig(BaseConfig):
    FLASK_SERVER_NAME = 'localhost:8888'
    FLASK_DEBUG = False  # Do not use debug mode in production
    PROD = True
    DB = 'prodb'


class DevelopmentConfig(BaseConfig):
    # Flask settings
    FLASK_SERVER_NAME = 'localhost:8888'
    FLASK_DEBUG = True  # Do not use debug mode in production
    DB = 'devdb'
    # Flask-Restplus settings
    SWALLOW_SWAGGER_UI_DOC_EXPANSION = 'list'
    SWALLOW_VALIDATE = True
    SWALLOW_MASK_SWAGGER = False
    SWALLOW_ERROR_404_HELP = False    

class TestingConfig(BaseConfig):
    TESTING = True
    DB = 'testdb'

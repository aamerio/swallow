# pylint: disable=missing-docstring

class BaseConfig(object):
    PATH_SUFFIX = "/api"
    DB = 'db'
    VERSION = '0.0.1'
    ENABLED_MODULES = (
        'mongodb',
    )

class ProductionConfig(BaseConfig):
    PROD = True
    DB = 'prodb'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DB = 'devdb'

class TestingConfig(BaseConfig):
    TESTING = True
    DB = 'testdb'

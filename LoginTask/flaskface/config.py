

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '123456789987456321'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

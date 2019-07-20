import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '4tUC^2AAUog3')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    DEBUG = True
    url = (
        "postgresql://guacamole:Test1234x@127.0.0.1:5432/guacamoledb"
    )
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    url = (
        "postgresql://guacamole:Test1234x@127.0.0.1:5432/guacamoletest_db"
    )
    SQLALCHEMY_DATABASE_URI = url
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

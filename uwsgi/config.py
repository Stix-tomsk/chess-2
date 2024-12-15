from os import getenv
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = getenv('DEBUG')
    CSRF_ENABLED = getenv('CSRF_ENABLED')
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = os.getenv('DEBUG')
    CSRF_ENABLED = os.getenv('CSRF_ENABLED')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pswd}@{host}:{port}'.format(
        user=os.getenv("DB_USER"),
        pswd=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
        )

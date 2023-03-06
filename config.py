import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


def as_bool(value):

    """Helper function that helpfully returns a boolean"""


    if value:
        return value.lower() in ['true', 'yes', 'on', '1']
    return False


class Config:

    """
    General Config class to store and load environment variables when creating flask app
    Provides some fallbacks if missing
    Dev env variables loaded via dotenv()
    
    """
    
    # database options

    #sqlalchemy config and sqlite fallback
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #alchemical config
    ALCHEMICAL_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    ALCHEMICAL_ENGINE_OPTIONS = {'echo': as_bool(os.environ.get('SQL_ECHO'))}

    # security options
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top-secret!')

    USE_CORS = as_bool(os.environ.get('USE_CORS') or 'yes')
    CORS_SUPPORTS_CREDENTIALS = True

    # email options
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or '25')
    MAIL_USE_TLS = as_bool(os.environ.get('MAIL_USE_TLS'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER',
                                       'donotreply@microblog.example.com')

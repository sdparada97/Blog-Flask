import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

#  CARGA LAS VARIABLES DE ENTORNO
load_dotenv('.env')

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+ os.getenv('USERNAME_DEV') +':'+ os.getenv('PASSWORD_DEV') +'@localhost:5432/'+ os.getenv('DBNAME_DEV')


# ENTORNOS DE EJECUCION
class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+ os.getenv('USERNAME_PRO') +':'+ os.getenv('PASSWORD_PRO') +'@localhost:5432/'+ os.getenv('DBNAME_PRO')

class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
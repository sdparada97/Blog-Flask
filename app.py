# IMPORTAR LIBRERIAS DE TERCEROS
import os
from flask import Flask
from dotenv import load_dotenv

# IMPORTAR BASE DE DATOS
from database import db


# IMPORTAR BLUEPRINTS
from apps.home.views import bp_home

#  CARGA LAS VARIABLES DE ENTORNO
load_dotenv('.env')

def create_app():
    app = Flask(__name__)

    # CONFIGURACION DEL PROYECTO POR AMBIENTE
    app.config.from_object(os.getenv('EXECUTE_ENV'))

    # setup all our dependencies
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # register blueprint
    app.register_blueprint(bp_home)

    return app

if __name__ == "__main__":
    create_app().run()
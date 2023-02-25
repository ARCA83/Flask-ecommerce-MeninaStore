from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate



load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')

conexion.init_app(app)

migrate = Migrate(app, conexion)

@app.before_first_request
def inicializadora():
    #conexion.create_all()
    pass

@app.route("/")
def index():
    return "Vamos con toda la concentracion"

import routers


if __name__ == '__main__':
    app.run(debug=True)

from app import app
from controllers.usuarios_controller import UsuariosController

from flask import request


@app.route("/auth/registrar", methods=['POST'])
def usuariosRegistrar():
    controllador = UsuariosController()
    return controllador.crearUsuario(request.json)

@app.route("/auth/listar", methods=['GET'])
def usuariosAutenticar():
    controller = UsuariosController()
    return controller.listarUsuario()

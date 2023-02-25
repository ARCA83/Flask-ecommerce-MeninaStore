from configuracion import conexion
from models.usuarios_model import UsuariosModel
from werkzeug.security import  generate_password_hash


class UsuariosController:
    def __init__(self) -> None:
        self.model = UsuariosModel

    def crearUsuario(self, data):
        try:
            contrasena = generate_password_hash(data['contrasena'])
            usuario = self.model(data['nombres'], data['correo'], data['imagen'], contrasena)
            conexion.session.add(usuario)
            conexion.session.commit()
            return {
                'data': usuario.convertirJson()
            }
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    def listarUsuario(self):
        try:
            usuarios = UsuariosModel.query.all()
            response = []
            for usuario in usuarios:
                response.append(usuario.convertirJson())
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

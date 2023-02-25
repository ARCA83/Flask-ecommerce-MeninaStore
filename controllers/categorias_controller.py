from configuracion import conexion
from models.categorias_model import CategoriasModel

class CategoriasController:
    def __init__(self) -> None:
        self.model = CategoriasModel

    def crearCategoria(self,data):
        try:
            categoria = self.model(data['nombre'])
            conexion.session.add(categoria)
            conexion.session.commit()
            return{
                'data':categoria.convertirJson()
            },201
            
        except Exception as e:
            conexion.session.rollback()
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500
        
    def listarCategorias(self):
        try:
            #categorias = CategoriasModel.query.all()
            categorias = self.model.query.filter_by(estado=True).all()
            response = []
            for categoria in categorias:
                response.append(categoria.convertirJson())                      
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
        
    def eliminarCategoria(self,categoria_id):
        try:
            categoria = CategoriasModel.query.filter_by(id=categoria_id).first()
            categoria.estado=False
            conexion.session.commit()
            return {
                'message': 'Categoria eliminada correctamente'
            }, 200
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    def actualizarCategoria(self,categoria_id,data):
        try:
            categoria = CategoriasModel.query.filter_by(id=categoria_id).first()
            categoria.nombre = data['nombre']
            conexion.session.commit()
            return {
                'data': categoria.convertirJson()
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
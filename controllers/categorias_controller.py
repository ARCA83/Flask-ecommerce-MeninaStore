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
        
    def listarCategorias(self,id):
        try:
            print(id)
            # categorias = self.model.query.all()
            categorias = self.model.query.filter_by(estado=True).all()
            # response = []
            # for categoria in categorias:
            #     response.append(categoria.convertirJson())

            response = [
                categoria.convertirJson()
                for categoria in categorias
            ]
            return {
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
        
            

from models.productos_model import ProductosModel
from models.categorias_productos_model import CategoriasProductosModel
from configuracion import conexion


class ProductosController:
    def __init__(self) -> None:
        self.model = ProductosModel

    def crearProducto(self, data):
        try:
            producto = self.model(data['nombre'], data['precio'], data['imagen'])
            conexion.session.add(producto)
            conexion.session.commit()

            nuevas_categorias = []
            for categoria in data['categorias']:
                nueva_categoria = CategoriasProductosModel(producto.id, categoria['categoria_id'])
                nuevas_categorias.append(nueva_categoria)
            conexion.session.add_all(nuevas_categorias)
            conexion.session.commit()
            
            return {
                'data': producto.convertirJson()
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def listarProductos(self):
        try:
            productos = ProductosModel.query.all()
            response = []
            for producto in productos:
                response.append(producto.convertirJson())
            return {
                'data': response
            }, 200
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def eliminarProductos(self, producto_id):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.estado=False
            conexion.session.commit()
           
            return {
                'message': 'Producto Eliminado Correctamente'
            }, 200
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarProducto(self, producto_id, data):
        try:
            producto = ProductosModel.query.filter_by(id=producto_id).first()
            producto.nombre = data['nombre']
            producto.precio = data['precio']
            producto.imagen = data['imagen']
            conexion.session.commit()

            return {
                'data': producto.convertirJson()
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
    def buscarProductos(self,precio):
        try:
            productos = ProductosModel.query.filter_by(precio=precio).all()
            response = []
            for producto in productos:
                response.append(producto.convertirJson())
        
            return {
                'data': response
            }, 200

        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500
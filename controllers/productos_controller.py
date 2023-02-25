from models.productos_model import ProductosModel
from configuracion import conexion


class ProductosController:

    def crearProducto(self, data):
        try:
            producto = ProductosModel(data['nombre'], data['precio']),data['imagen']
            conexion.session.add(producto)
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
                response.append({producto.convertirJson()})
            return {
                'message': productos
            }, 200
        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def eliminarProductos(self, producto_id):
        try:
            producto = ProductosModel.query.filer_by(id=producto_id).first()
            producto.estado=False
            conexion.session.commit()
            print(producto)
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
            conexion.session.commit()
            print(producto)
            print(data)

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
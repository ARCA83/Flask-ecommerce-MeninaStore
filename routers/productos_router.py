from app import app
from controllers.productos_controller import ProductosController
from flask import request


@app.route("/productos/crear", methods=['POST'])
def productosCrear():
    controller = ProductosController()
    return controller.crearProducto(request.get_json())


@app.route("/productos/lista", methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.listarProductos()


@app.route("/productos/eliminar/<int:producto_id>", methods=['DELETE'])
def productosEliminar(producto_id):
    controller = ProductosController()
    return controller.eliminarProductos(producto_id)


@app.route("/productos/actualizar/<int:producto_id>", methods=['PUT'])
def productosActualizar(producto_id):
    controller = ProductosController()
    return controller.actualizarProducto(producto_id, request.json)

@app.route("/productos/buscar/<float:precio>", methods=['GET'])
def productosBuscar(precio):
    controller = ProductosController()
    return controller.buscarProductos(precio)
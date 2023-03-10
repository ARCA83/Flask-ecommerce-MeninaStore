from app import app
from controllers.categorias_controller import CategoriasController
from flask import request

@app.route("/categorias/crear", methods=['POST'])
def categoriasCrear():
    controller = CategoriasController()
    return controller.crearCategoria(request.json)

@app.route("/categorias/listar", methods=['GET'])
def categoriasListar():
    controller = CategoriasController()
    return controller.listarCategorias()

@app.route("/categorias/eliminar/<int:categoria_id>", methods=['DELETE'])
def categoriaEliminar(categoria_id):
    controller = CategoriasController()
    return controller.eliminarCategoria(categoria_id)

@app.route("/categorias/actualizar/<int:categoria_id>", methods=['PUT'])
def categoriaActualizar(categoria_id):
    controller = CategoriasController()
    return controller.actualizarCategoria(categoria_id,request.json)
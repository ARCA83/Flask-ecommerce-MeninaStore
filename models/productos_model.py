from configuracion import conexion
from sqlalchemy import Column,Integer, String,Float,Text, Boolean

class ProductosModel(conexion.Model):
    __talename__='productos'

    id= Column(Integer,primary_key=True,autoincrement=True)
    nombre=Column(String(45),nullable=False,unique=True)
    precio=Column(Float(),nullable=False)
    imagen=Column(Text,nullable=False )
    estado=Column(Boolean, default=True)

    def __init__(self, nombre, precio, imagen, estado=None) -> None:
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.estado = estado

    

    def convertirJson(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'precio':self.precio,
            'imagen':self.imagen,
            'estado':self.estado,
            #'categorias': categorias_productos
        }
from configuracion import conexion
from sqlalchemy import Column,Integer, String, Boolean

class CategoriasModel(conexion.Model):
    __talename__='categorias'

    id= Column(Integer,primary_key=True,autoincrement=True,unique=True)
    nombre = Column(String(90),nullable=False)
    estado = Column(Boolean, default=True)

    def __init__(self, nombre, estado=None) -> None:
        self.nombre = nombre
        self.estado = estado
    def convertirJson(self):
        return{
            'id':self.id,
            'nombre':self.nombre
        }
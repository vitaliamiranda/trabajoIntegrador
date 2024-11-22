from Collection import Coleccion

class Database:

    def __init__(self,nombre):
        self.nombre = nombre
        self.coleccion = Coleccion("alternativo")

    def create_collection(self,nombre_coleccion):
        self.coleccion = Coleccion(nombre_coleccion)

    def get_collection(self,nombre_coleccion) -> Coleccion:
        if self.coleccion.get_nombre() == nombre_coleccion:
            return self.coleccion
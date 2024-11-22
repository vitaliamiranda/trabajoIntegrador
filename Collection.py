from Str2Dict import Str2Dic
from Documento import Documento
import os.path as path

class Coleccion:
    def __init__(self,nombre):
        self.nombre = nombre
        self.contenido = {}

    def get_nombre(self):
        return self.nombre

    def mostrar_documentos(self):
        return self.contenido
    
    def get_document(self,doc_id) -> Documento:
        datos = self.contenido
        if datos.get(int(doc_id)):
            busqueda = datos[int(doc_id)].get_documento()
            return busqueda

    def list_documents(self) -> dict:
        return self.contenido

    def delete_document(self,doc_id):
        datos = self.contenido
        busqueda = str(datos[int(doc_id)].get_documento())
        print("Esta es el documento a eliminar" + busqueda)
        del datos[int(doc_id)]
        self.contenido = datos
        print("Se elimino correctamente")

    def import_csv(self,nombre_coleccion, ruta_csv):
        if nombre_coleccion == self.nombre:
            if path.isfile(ruta_csv): 
                with open(ruta_csv) as archivo:
                    primera_linea = archivo.readline()
                    schema = primera_linea.replace("\n","").split(",")

                documeto = Str2Dic(schema)

                with open(ruta_csv) as csvFile:
                    lienas = csvFile.readlines()

                diccionario = {}
                coleccion = {}
            
                for i in range(1,len(lienas)):
                    datos = lienas[i].replace("\n","").split(",")
                    diccionario = documeto.convert(datos,i)
                    coleccion[i] = diccionario

                self.contenido = coleccion
                print("se importaron los datos correctamente")
            else:
                print("Esta ruta no corresponde a un arc")
        else:
            print("El nombre de la coleccion es incorrecto")
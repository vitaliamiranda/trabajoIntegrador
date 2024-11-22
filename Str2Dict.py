from Documento import Documento

class Str2Dic:
    def __init__(self, schema: str):
       self.schema = schema
    
    def convert(self,datos: str, id: int):
        datos_schema = self.schema

        diccionario = dict()

        for i in range(len(datos_schema)):
            diccionario["id"] = id
            diccionario[datos_schema[i]] = datos[i]

        diccionario_inicio = Documento(id,diccionario)
        return diccionario_inicio

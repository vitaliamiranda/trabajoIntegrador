class Documento:
    def __init__(self,id: int,contenido:dict):
        self.id = id
        self.contenido = contenido if contenido != None else {}

    def set_documento(self, contenido: dict) -> None:
        self.contenido = contenido

    def get_documento(self) -> dict:
        return self.contenido
    
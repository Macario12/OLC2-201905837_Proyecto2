#Simbolo posee idi, valor y un tipo
from Enum.tipoSimbolo import tipoSimbolo


class Simbolo:
    def __init__(self, id: str, type,position):
        self.id = id
        self.type = type
        self.tipoSimbolo = tipoSimbolo.Variable
        self.position = position
    def getId(self):
        return self.id

    def getType(self):
        return self.type
        
    def getTipoSimbolo(self):
        return self.tipoSimbolo

    def setType(self,type):
        self.type = type
        
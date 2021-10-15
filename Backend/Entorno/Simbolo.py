#Simbolo posee idi, valor y un tipo
from Enum.tipoSimbolo import tipoSimbolo


class Simbolo:
    def __init__(self, id: str, value, type):
        self.id = id
        self.value = value
        self.type = type
        self.tipoSimbolo = tipoSimbolo.Variable

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def getType(self):
        return self.type
        
    def getTipoSimbolo(self):
        return self.tipoSimbolo

    def setValue(self,value):
        self.value = value
    def setType(self,type):
        self.type = type
        
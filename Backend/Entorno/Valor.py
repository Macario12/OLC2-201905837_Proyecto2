from Enum.tipoExpresion import tipoExpresion

class Value:
    def __init__(self,value:str, isTemp:bool, type: tipoExpresion) -> None:
        self.value = value
        self.isTemp = isTemp
        self.type = type
        self.trueLabel = ""
        self.falseLabel = ""

    def getValue(self) -> str:
        return self.value
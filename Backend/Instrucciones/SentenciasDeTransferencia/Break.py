from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Break(Instruction):

    def __init__(self) -> None:
        super().__init__()
        self.label = ""

    def compile(self, entorno: Environment) -> Value:
        
        self.generator.addIf("1","1","==",self.label)


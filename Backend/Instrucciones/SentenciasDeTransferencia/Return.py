from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Return(Instruction):

    def __init__(self, expresion:Expresion) -> None:
        super().__init__()
        self.expresion = expresion

    def compile(self, entorno: Environment) -> Value:
        
        self.expresion.generator = self.generator

        return self.expresion.compile(entorno)

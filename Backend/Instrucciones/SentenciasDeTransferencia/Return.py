from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Return(Instruction):

    def __init__(self, expresion:Expresion) -> None:
        super().__init__()
        self.expresion = expresion
        self.labelReturn  = ""
        self.hayreturn = False

    def compile(self, entorno: Environment) -> Value:
        
        self.expresion.generator = self.generator
        expresionReturn = self.expresion.compile(entorno)
        tempReturn = self.generator.newTemp()
        self.generator.addComentario("Return")
        self.generator.addExpression(tempReturn,"P","0","+")
        self.generator.addSetStack(tempReturn,expresionReturn.getValue())
        self.generator.addIf("1","1","==",self.labelReturn)

        self.hayreturn = True

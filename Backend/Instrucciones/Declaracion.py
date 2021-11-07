from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Declaracion(Instruction):

    def __init__(self, id, exp:Expresion,tipo:tipoExpresion) -> None:
        super().__init__()
        self.id = id
        self.expresion = exp
        self.tipo = tipo

    def compile(self, entorno: Environment) -> Value:

        self.expresion.generator = self.generator

        nuevoValor: Value = self.expresion.compile(entorno)

        tempVar: Simbolo = entorno.saveVariable(self.id,self.tipo)

        if self.tipo != tipoExpresion.BOOL:
            self.generator.addSetStack(str(tempVar.position), nuevoValor.getValue())

        else:
            nuevoLabel = self.generator.newLabel()
            nuevoLabel2 = self.generator.newLabel()
            nuevoLabel3 = self.generator.newLabel()
            self.generator.addIf(nuevoValor.getValue(),"1","==",nuevoLabel)
            self.generator.addGoto(nuevoLabel2)
            self.generator.addLabel(nuevoLabel)
            self.generator.addSetStack(str(tempVar.position),'1')
            self.generator.addGoto(nuevoLabel3)
            self.generator.addLabel(nuevoLabel2)
            self.generator.addSetStack(str(tempVar.position),'0')
            self.generator.addLabel(nuevoLabel3)
        #return super().compile(entorno)
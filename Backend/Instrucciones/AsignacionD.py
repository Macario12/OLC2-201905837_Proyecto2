from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Asignacion(Instruction):

    def __init__(self, id, exp:Expresion) -> None:
        super().__init__()
        self.id = id
        self.expresion = exp

    def compile(self, entorno: Environment) -> Value:

        self.expresion.generator = self.generator

        nuevoValor: Value = self.expresion.compile(entorno)

        variableE:  Simbolo =  entorno.getVariable(self.id)

        if variableE != None:
            tempVar: Simbolo = entorno.updateVariable(self.id,nuevoValor.type)
            if nuevoValor.type != tipoExpresion.BOOL:
                self.generator.addSetStack(str(tempVar.position), nuevoValor.getValue())

            else:
                nuevoLabel = self.generator.newLabel()

                self.generator.addLabel(nuevoValor.trueLabel)
                self.generator.addSetStack(str(tempVar.position),'1')
                self.generator.addGoto(nuevoLabel)
                self.generator.addLabel(nuevoValor.falseLabel)
                self.generator.addSetStack(str(tempVar.position),'0')
                self.generator.addLabel(nuevoLabel)
            
        else:
            tempVar: Simbolo = entorno.saveVariable(self.id,nuevoValor.type)


            if nuevoValor.type != tipoExpresion.BOOL:
                self.generator.addSetStack(str(tempVar.position), nuevoValor.getValue())

            else:
                nuevoLabel = self.generator.newLabel()

                self.generator.addLabel(nuevoValor.trueLabel)
                self.generator.addSetStack(str(tempVar.position),'1')
                self.generator.addGoto(nuevoLabel)
                self.generator.addLabel(nuevoValor.falseLabel)
                self.generator.addSetStack(str(tempVar.position),'0')
                self.generator.addLabel(nuevoLabel)


        #return super().compile(entorno)
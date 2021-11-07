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
                temporalAsignacion = self.generator.newTemp()
                self.generator.addExpression(temporalAsignacion,"P",str(tempVar.position),"+")
                self.generator.addSetStack(temporalAsignacion, nuevoValor.getValue())

            else:
                temporalAsignacion = self.generator.newTemp()
                self.generator.addExpression(temporalAsignacion,"P",str(tempVar.position),"+")
                
                nuevoLabel = self.generator.newLabel()
                nuevoLabel2 = self.generator.newLabel()
                nuevoLabel3 = self.generator.newLabel()
                self.generator.addIf(nuevoValor.getValue(),"1","==",nuevoLabel)
                self.generator.addGoto(nuevoLabel2)
                self.generator.addLabel(nuevoLabel)
                self.generator.addSetStack(temporalAsignacion,'1')
                self.generator.addGoto(nuevoLabel3)
                self.generator.addLabel(nuevoLabel2)
                self.generator.addSetStack(temporalAsignacion,'0')
                self.generator.addLabel(nuevoLabel3)
            
        else:
            tempVar: Simbolo = entorno.saveVariable(self.id,nuevoValor.type)


            if nuevoValor.type != tipoExpresion.BOOL:
                temporalAsignacion = self.generator.newTemp()
                self.generator.addExpression(temporalAsignacion,"P",str(tempVar.position),"+")
                self.generator.addSetStack(temporalAsignacion, nuevoValor.getValue())

            else:

                
                temporalAsignacion = self.generator.newTemp()
                self.generator.addExpression(temporalAsignacion,"P",str(tempVar.position),"+")
                
                nuevoLabel = self.generator.newLabel()
                nuevoLabel2 = self.generator.newLabel()
                nuevoLabel3 = self.generator.newLabel()
                self.generator.addIf(nuevoValor.getValue(),"1","==",nuevoLabel)
                self.generator.addGoto(nuevoLabel2)
                self.generator.addLabel(nuevoLabel)
                self.generator.addSetStack(temporalAsignacion,'1')
                self.generator.addGoto(nuevoLabel3)
                self.generator.addLabel(nuevoLabel2)
                self.generator.addSetStack(temporalAsignacion,'0')
                self.generator.addLabel(nuevoLabel3)


        #return super().compile(entorno)
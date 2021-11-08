from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion
from Enum.tipoEntorno import tipoEntorno

class Asignacion(Instruction):

    def __init__(self, id, exp:Expresion,tipoEntorno) -> None:
        super().__init__()
        self.id = id
        self.expresion = exp
        self.tipoEntorno = tipoEntorno

    def compile(self, entorno: Environment) -> Value:

        self.expresion.generator = self.generator

        nuevoValor: Value = self.expresion.compile(entorno)
        validacionesDelcaracion(self,nuevoValor,entorno)


def validacionesDelcaracion(self,nuevoValor,entorno):
    if self.tipoEntorno == None or self.tipoEntorno == tipoEntorno.LOCAL:
        if entorno.nombre == "funcion" or entorno.nombre == "global":
            if(entorno.existeVariableEntornoActual(self.id)):
                tempVar: Simbolo = entorno.saveVariable(self.id,nuevoValor.type)
                c3dDeclaracion(self,tempVar,nuevoValor)
            else:
                tempVar: Simbolo = entorno.updateVariable(self.id,nuevoValor.type)
                c3dDeclaracion(self,tempVar,nuevoValor)
        elif entorno.nombre == "ciclo":
            if self.tipoEntorno == tipoEntorno.LOCAL or self.tipoEntorno == None:
                if entorno.existeVariableEntornoActual(self.id):
                    tempVar: Simbolo = entorno.saveVariable(self.id,nuevoValor.type)
                    c3dDeclaracion(self,tempVar,nuevoValor)
                else:
                    tempVar: Simbolo = entorno.updateVariable(self.id,nuevoValor.type)
                    c3dDeclaracion(self,tempVar,nuevoValor)

            else:
                if(entorno.existeVariable(self.id)):
                    tempVar: Simbolo = entorno.saveVariable(self.id,nuevoValor.type)
                    c3dDeclaracion(self,tempVar,nuevoValor)
                else:
                    tempVar: Simbolo = entorno.updateVariable(self.id,nuevoValor.type)
                    c3dDeclaracion(self,tempVar,nuevoValor)
    elif self.tipoEntorno == tipoEntorno.GLOBAL:
        entornoG = entorno.getEntornoGlobal()

        if(entornoG.existeVariableEntornoActual(self.id)):
            tempVar: Simbolo = entornoG.saveVariable(self.id,nuevoValor.type)
            c3dDeclaracion(self,tempVar,nuevoValor)
        else:
            tempVar: Simbolo = entornoG.updateVariable(self.id,nuevoValor.type)
            c3dDeclaracion(self,tempVar,nuevoValor)


def c3dDeclaracion(self,tempVar,nuevoValor):
    if nuevoValor.type != tipoExpresion.BOOL:
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
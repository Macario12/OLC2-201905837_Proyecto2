from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion
from Enum.tipoEntorno import tipoEntorno

class Declaracion(Instruction):

    def __init__(self, id, exp:Expresion,tipo:tipoExpresion,tipoEntorno:tipoEntorno) -> None:
        super().__init__()
        self.id = id
        self.expresion = exp
        self.tipo = tipo
        self.tipoEntorno = tipoEntorno

    def compile(self, entorno: Environment) -> Value:

        

        self.expresion.generator = self.generator

        nuevoValor: Value = self.expresion.compile(entorno)

        
        if self.tipo == tipoExpresion.INTEGER:
            if nuevoValor.type == tipoExpresion.INTEGER:
                validacionesDelcaracion(self,nuevoValor,entorno)
        if self.tipo == tipoExpresion.FLOAT:
            if nuevoValor.type == tipoExpresion.FLOAT:
                validacionesDelcaracion(self,nuevoValor,entorno)
        if self.tipo == tipoExpresion.STRING:
            if nuevoValor.type == tipoExpresion.STRING:
                validacionesDelcaracion(self,nuevoValor,entorno)
        if self.tipo == tipoExpresion.CHAR:
            if nuevoValor.type == tipoExpresion.CHAR:
                validacionesDelcaracion(self,nuevoValor,entorno)
        if self.tipo == tipoExpresion.BOOL:
            if nuevoValor.type == tipoExpresion.BOOL:
                validacionesDelcaracion(self,nuevoValor,entorno)
        
        #return super().compile(entorno)

def validacionesDelcaracion(self,nuevoValor,entorno):
    if self.tipoEntorno == None or self.tipoEntorno == tipoEntorno.LOCAL:
        if entorno.nombre == "funcion" or entorno.nombre == "global":
            if(entorno.existeVariableEntornoActual(self.id)):
                tempVar: Simbolo = entorno.saveVariable(self.id,self.tipo)
                c3dDeclaracion(self,tempVar,nuevoValor)
            else:
                tempVar: Simbolo = entorno.updateVariable(self.id,self.tipo)
                c3dDeclaracion(self,tempVar,nuevoValor)
        elif entorno.nombre == "ciclo":
            if self.tipoEntorno == tipoEntorno.LOCAL:
                if entorno.existeVariableEntornoActual(self.id):
                    tempVar: Simbolo = entorno.saveVariable(self.id,self.tipo)
                    c3dDeclaracion(self,tempVar,nuevoValor)
                else:
                    tempVar: Simbolo = entorno.updateVariable(self.id,self.tipo)
                    c3dDeclaracion(self,tempVar,nuevoValor)

            else:
                if(entorno.existeVariable(self.id)):
                    tempVar: Simbolo = entorno.saveVariable(self.id,self.tipo)
                    c3dDeclaracion(self,tempVar,nuevoValor)
                else:
                    tempVar: Simbolo = entorno.updateVariable(self.id,self.tipo)
                    c3dDeclaracion(self,tempVar,nuevoValor)
    elif self.tipoEntorno == tipoEntorno.GLOBAL:
        entornoG = entorno.getEntornoGlobal()

        if(entornoG.existeVariableEntornoActual(self.id)):
            tempVar: Simbolo = entornoG.saveVariable(self.id,self.tipo)
            c3dDeclaracion(self,tempVar,nuevoValor)
        else:
            tempVar: Simbolo = entornoG.updateVariable(self.id,self.tipo)
            c3dDeclaracion(self,tempVar,nuevoValor)


def c3dDeclaracion(self,tempVar,nuevoValor):
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
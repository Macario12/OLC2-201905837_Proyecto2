import math
from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Environment
from Abstract.Expresion import Expresion
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Potencia(Expresion):
    def __init__(self,left: Expresion,right:Expresion) -> None:
        super().__init__()
        self.izqExpresion = left
        self.derExpresion = right

    def compile(self, entorno: Environment) -> Value:
        
        self.izqExpresion.generator = self.generator
        self.derExpresion.generator = self.generator

        ValorIzq: Value = self.izqExpresion.compile(entorno)
        Valorder: Value = self.derExpresion.compile(entorno)
        
        if ValorIzq.type == tipoExpresion.INTEGER or ValorIzq.type == tipoExpresion.FLOAT:
            if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                tempCambioSimulado = self.generator.newTemp()

                self.generator.addExpression(tempCambioSimulado,"P",str(entorno.size),"+")

                nuevoTmp = self.generator.newTemp()
                self.generator.addExpression(nuevoTmp,tempCambioSimulado,str(1),"+")
                self.generator.addSetStack(nuevoTmp,ValorIzq.getValue())
                
                nuevoTmp = self.generator.newTemp()
                self.generator.addExpression(nuevoTmp,tempCambioSimulado,str(2),"+")
                self.generator.addSetStack(nuevoTmp,Valorder.getValue())

                ##LLamada de la funcion
                funcG: Simbolo = entorno.getFunction("potenciaNativas")
                self.generator.addNextStack(str(entorno.size))
                self.generator.addCallFunc("potenciaNativas")
                #Temporal para el retorno
                tmpReturn = self.generator.newTemp()
                self.generator.addGetStack(tmpReturn,"P")
                self.generator.addBackStack(str(entorno.size))

                
                return Value(str(tmpReturn),True,ValorIzq.type)

        if ValorIzq.type == tipoExpresion.STRING:
            if Valorder.type == tipoExpresion.INTEGER:
                tempCambioSimulado = self.generator.newTemp()

                self.generator.addExpression(tempCambioSimulado,"P",str(entorno.size),"+")

                nuevoTmp = self.generator.newTemp()
                self.generator.addExpression(nuevoTmp,tempCambioSimulado,str(1),"+")
                self.generator.addSetStack(nuevoTmp,ValorIzq.getValue())
                
                nuevoTmp = self.generator.newTemp()
                self.generator.addExpression(nuevoTmp,tempCambioSimulado,str(2),"+")
                self.generator.addSetStack(nuevoTmp,Valorder.getValue())

                ##LLamada de la funcion
                funcG: Simbolo = entorno.getFunction("potenciaStringNativas")
                self.generator.addNextStack(str(entorno.size))
                self.generator.addCallFunc("potenciaStringNativas")
                #Temporal para el retorno
                tmpReturn = self.generator.newTemp()
                self.generator.addGetStack(tmpReturn,"P")
                self.generator.addBackStack(str(entorno.size))

                
                return Value(str(tmpReturn),True,funcG.getType())


                

from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Simbolo import Simbolo
from Instrucciones.SentenciasDeTransferencia.Return import Return
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class LLamadaFuncion(Instruction):

    def __init__(self, id,valores) -> None:
        super().__init__()
        self.id = id
        self.parametros = valores
        

    def compile(self, entorno: Environment) -> Value:
        #Cambio simulado de ambito.

        tempCambioSimulado = self.generator.newTemp()
        self.generator.addExpression(tempCambioSimulado,"P",str(entorno.size),"+")

        if self.parametros != None:
            contador = 1
            for parametro in self.parametros:
                parametro.generator = self.generator
                tmp = parametro.compile(entorno)
                nuevoTmp = self.generator.newTemp()
                self.generator.addExpression(nuevoTmp,tempCambioSimulado,str(contador),"+")
                self.generator.addSetStack(nuevoTmp,tmp.getValue())
                contador = contador + 1

        ##LLamada de la funcion
        funcG: Simbolo = entorno.getFunction(self.id)
        self.generator.addNextStack(str(entorno.size))
        self.generator.addCallFunc(self.id)
        #Temporal para el retorno
        tmpReturn = self.generator.newTemp()
        self.generator.addGetStack(tmpReturn,"P")
        self.generator.addBackStack(str(entorno.size))

        
        return Value(str(tmpReturn),True,funcG.getType())

            
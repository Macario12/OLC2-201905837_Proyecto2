from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class StringNative(Expresion):
    def __init__(self, valor) -> None:
        super().__init__()
        self.tipo = tipoExpresion.STRING
        self.valor = valor

    def compile(self, entorno: Environment) -> Value:

        try:

            if self.tipo == tipoExpresion.STRING:
                asTmp = self.generator.newTemp()
                self.generator.addAsig(asTmp,"H")
                valorStrng = str(self.valor.getValue())
                for character in valorStrng:
                    self.generator.addSetHeap("H",str(ord(character)))
                    self.generator.addNextHeap()
                
                self.generator.addSetHeap("H",str(-1))
                self.generator.addNextHeap()
                #tempVar: Simbolo =entorno.saveVariable(self.valor,tipoExpresion.STRING)
                #self.generator.addSetStack(str(tempVar.position),asTmp)

                #entorno.saveVariable(self.valor,tipoExpresion.STRING)

                return Value(str(str(asTmp)),False,tipoExpresion.STRING)
            
        except:
            print('No se reconoce el valor string')
            return Value("0",False,tipoExpresion.STRING)
    
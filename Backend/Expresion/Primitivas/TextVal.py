from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class TextVal(Expresion):
    def __init__(self,tipo:tipoExpresion, valor) -> None:
        super().__init__()
        self.tipo = tipo
        self.valor = valor

    def compile(self, entorno: Environment) -> Value:

        try:

            if self.tipo == tipoExpresion.STRING:
                asTmp = self.generator.newTemp()
                self.generator.addAsig(asTmp,"H")
                for character in self.valor:
                    self.generator.addSetHeap("H",str(ord(character)))
                    self.generator.addNextHeap()
                
                self.generator.addSetHeap("H",str(-1))
                self.generator.addNextHeap()
                #tempVar: Simbolo =entorno.saveVariable(self.valor,tipoExpresion.STRING)
                #self.generator.addSetStack(str(tempVar.position),asTmp)

                #entorno.saveVariable(self.valor,tipoExpresion.STRING)

                return Value(str(str(asTmp)),False,self.tipo)

            elif self.tipo == tipoExpresion.CHAR:
                for character in self.valor:
                    return Value(str(ord(character)),False,self.tipo)

            
        except:
            print('No se reconoce el valor string')
            return Value("0",False,tipoExpresion.STRING)
    
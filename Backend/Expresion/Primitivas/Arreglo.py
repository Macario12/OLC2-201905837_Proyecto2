from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Arreglo(Expresion):
    def __init__(self,tipo:tipoExpresion, listaDeValores) -> None:
        super().__init__()
        self.tipo = tipo
        self.listaDeValores = listaDeValores

    def compile(self, entorno: Environment) -> Value:

        try:

            if self.tipo == tipoExpresion.ARREGLO:
                asTmp = self.generator.newTemp()
                self.generator.addAsig(asTmp,"H")
                self.generator.addSetHeap("H",str(len(self.listaDeValores)))
                self.generator.addNextHeap()
                valores = []
                for valor in self.listaDeValores:
                    valor_ = valor.compile(entorno)
                    valores.append(valor_.value)

                for valor in valores:
                    self.generator.addSetHeap("H",str(valor))
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
    
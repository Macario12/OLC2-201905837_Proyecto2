from Abstract.Expresion import Expresion
from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class UpperCase(Expresion):
    def __init__(self,tipo:tipoExpresion, expresion:Expresion) -> None:
        super().__init__()
        self.tipo = tipo
        self.expresion = expresion

    def compile(self, entorno: Environment) -> Value:

        #try:
            
            self.expresion.generator = self.generator
            indice = self.expresion.compile(entorno)
            if self.tipo == tipoExpresion.STRING:

                nuevaLabel = self.generator.newLabel()
                nuevaLabel2 = self.generator.newLabel()
                false = self.generator.newLabel()
                true = self.generator.newLabel()

                temp1 = self.generator.newTemp()
                temp2 = self.generator.newTemp()
            
                asTmp = self.generator.newTemp()
                self.generator.addAsig(asTmp,"H")

                temporal = self.generator.newTemp()
                self.generator.addExpression(temporal,indice.value,"0","+")
                self.generator.addLabel(false)
                self.generator.addGetHeap(temp1,temporal)
                self.generator.addIf(temp1,"-1","==",true)
                self.generator.addExpression(temp2,temp1,"32","-")
                self.generator.addIf(temp2,"65","<",nuevaLabel)
                self.generator.addIf(temp2,"90",">",nuevaLabel)
                self.generator.addSetHeap("H",temp2)
                self.generator.addGoto(nuevaLabel2)
                self.generator.addLabel(nuevaLabel)
                self.generator.addSetHeap("H",temp1)
                self.generator.addLabel(nuevaLabel2)
                self.generator.addNextHeap()
                self.generator.addExpression(temporal,temporal,"1","+")
                self.generator.addGoto(false)
    
                self.generator.addLabel(true)
                self.generator.addSetHeap("H",str(-1))
                self.generator.addNextHeap()

                return Value(str(asTmp),True,tipoExpresion.STRING)

            
        #except:
            #print('No se reconoce el valor string')
           # return Value("0",False,tipoExpresion.STRING)
    
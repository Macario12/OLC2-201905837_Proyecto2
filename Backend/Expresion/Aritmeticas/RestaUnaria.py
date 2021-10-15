from typing import AbstractSet
from Entorno.Entorno import Environment
from Abstract.Expresion import Expresion
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class RestaU(Expresion):
    def __init__(self,exp:Expresion) -> None:
        super().__init__()
        self.exp = exp
        

    def compile(self, entorno: Environment) -> Value:
        
        self.exp.generator = self.generator

        Valorexp: Value = self.exp.compile(entorno)
        

        tmp = self.generator.newTemp()


        if Valorexp.type  == tipoExpresion.INTEGER:
            
            self.generator.addExpression(tmp,"0",Valorexp.getValue(),"-")
            return Value(tmp,True,Valorexp.type)

        elif Valorexp.type  == tipoExpresion.FLOAT:
            
            self.generator.addExpression(tmp,0,Valorexp.getValue(),"-")
            return Value(tmp,True,tipoExpresion.FLOAT)
        else:
            print("ERROR EN LA MUL")
            return Value("0",False,tipoExpresion.INTEGER)
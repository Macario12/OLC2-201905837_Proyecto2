from typing import AbstractSet
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
        contador = 2;
        tmpAnterior = "";
        while contador <= int(Valorder.getValue()):
            tmp = self.generator.newTemp()

            if ValorIzq.type  == tipoExpresion.INTEGER:
                if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                    if contador> 2:
                        self.generator.addExpression(tmp,tmpAnterior,ValorIzq.getValue(),"*")    
                    else:
                        self.generator.addExpression(tmp,ValorIzq.getValue(),ValorIzq.getValue(),"*")
                    tmpAnterior = tmp
                    contador = contador +1

                else:
                    print("ERROR EN LA MUL")
                    return Value("0",False,tipoExpresion.INTEGER)

            elif ValorIzq.type  == tipoExpresion.FLOAT:
                if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                    if contador> 2:
                        self.generator.addExpression(tmp,tmpAnterior,ValorIzq.getValue(),"*")    
                    else:
                        self.generator.addExpression(tmp,ValorIzq.getValue(),ValorIzq.getValue(),"*")
                    tmpAnterior = tmp
                    contador = contador +1

                else:
                    print("ERROR EN LA MUL")
                    return Value("0",False,tipoExpresion.FLOAT)

            else:
                print("ERROR EN LA MUL")
                return Value("0",False,tipoExpresion.INTEGER)

        return Value(tmp,True,ValorIzq.type)
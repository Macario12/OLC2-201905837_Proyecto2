from typing import AbstractSet
from Entorno.Entorno import Environment
from Abstract.Expresion import Expresion
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Modulo(Expresion):
    def __init__(self,left: Expresion,right:Expresion) -> None:
        super().__init__()
        self.izqExpresion = left
        self.derExpresion = right

    def compile(self, entorno: Environment) -> Value:
        
        self.izqExpresion.generator = self.generator
        self.derExpresion.generator = self.generator

        ValorIzq: Value = self.izqExpresion.compile(entorno)
        Valorder: Value = self.derExpresion.compile(entorno)

        tmp = self.generator.newTemp()


        if ValorIzq.type  == tipoExpresion.INTEGER:
            if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                self.generator.addModulo(tmp,ValorIzq.getValue(),Valorder.getValue())
                return Value(tmp,True,Valorder.type)

            else:
                print("ERROR EN LA Mod")
                return Value("0",False,tipoExpresion.INTEGER)

        elif ValorIzq.type  == tipoExpresion.FLOAT:
            if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                self.generator.addModulo(tmp,ValorIzq.getValue(),Valorder.getValue())
                return Value(tmp,True,tipoExpresion.FLOAT)

            else:
                print("ERROR EN LA MUL")
                return Value("0",False,tipoExpresion.FLOAT)

        else:
            print("ERROR EN LA MUL")
            return Value("0",False,tipoExpresion.INTEGER)
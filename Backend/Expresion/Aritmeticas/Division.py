from typing import AbstractSet
from Entorno.Entorno import Environment
from Abstract.Expresion import Expresion
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Division(Expresion):
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
        self.trueLabel = self.generator.newLabel()
        
        self.falseLabel = self.generator.newLabel()

        if ValorIzq.type  == tipoExpresion.INTEGER:
            if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                
                self.generator.addIf(Valorder.getValue(),"0","!=",self.trueLabel)
                self.generator.addPrintfString("c","MathError")
                self.generator.addNewLine()
                self.generator.addGoto(self.falseLabel)
                self.generator.addLabel(self.trueLabel)
                self.generator.addExpression(tmp,"float64("+ValorIzq.getValue()+")","float64("+Valorder.getValue()+")","/")
                self.generator.addLabel(self.falseLabel)
                return Value(tmp,True,tipoExpresion.FLOAT)

            else:
                print("ERROR EN LA DIV")
                return Value("0",False,tipoExpresion.INTEGER)

        elif ValorIzq.type  == tipoExpresion.FLOAT:
            if Valorder.type == tipoExpresion.INTEGER or Valorder.type == tipoExpresion.FLOAT:
                self.generator.addIf(Valorder.getValue(),"0","!=",self.trueLabel)
                self.generator.addPrintfString("c","MathError")
                self.generator.addNewLine()
                self.generator.addGoto(self.falseLabel)
                self.generator.addLabel(self.trueLabel)
                self.generator.addExpression(tmp,"float64("+ValorIzq.getValue()+")","float64("+Valorder.getValue()+")","/")
                self.generator.addLabel(self.falseLabel)
                return Value(tmp,True,tipoExpresion.FLOAT)

            else:
                print("ERROR EN LA DIV")
                return Value("0",False,tipoExpresion.FLOAT)

        else:
            print("ERROR EN LA DIV")
            return Value("0",False,tipoExpresion.INTEGER)
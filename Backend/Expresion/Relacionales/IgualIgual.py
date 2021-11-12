from Abstract.Expresion import Expresion
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion


class IgualIgual(Expresion):

    def __init__(self, izquierda:Expresion, derecha:Expresion) -> None:
        super().__init__()
        self.izqExpresion = izquierda
        self.drhExpresion = derecha

    def compile(self, entorno: Environment) -> Value:

        self.izqExpresion.generator = self.generator
        self.drhExpresion.generator = self.generator

        izqValor: Value = self.izqExpresion.compile(entorno)
        drhValor: Value = self.drhExpresion.compile(entorno)

        if izqValor.type == tipoExpresion.INTEGER or izqValor.type == tipoExpresion.FLOAT or izqValor.type == tipoExpresion.BOOL:
            if drhValor.type == tipoExpresion.INTEGER or drhValor.type == tipoExpresion.FLOAT or drhValor.type == tipoExpresion.BOOL:
                
                newtemp = self.generator.newTemp()
                nuevoValor = Value(newtemp,True,tipoExpresion.BOOL)

                if self.trueLabel == "":
                    self.trueLabel = self.generator.newLabel()

                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()

                self.generator.addIf(izqValor.value, drhValor.value, "==",self.trueLabel)

                self.generator.addGoto(self.falseLabel)

                nuevoValor.trueLabel = self.trueLabel
                nuevoValor.falseLabel = self.falseLabel

                newLabel = self.generator.newLabel()
                
                self.generator.addLabel(nuevoValor.trueLabel)
                self.generator.addAsig(newtemp,"1")

                self.generator.addGoto(newLabel)
                self.generator.addLabel(nuevoValor.falseLabel)
                self.generator.addAsig(newtemp,"0")

                self.generator.addLabel(newLabel)
                return nuevoValor
        elif izqValor.type == tipoExpresion.STRING:
            if drhValor.type == tipoExpresion.STRING:
                
                newtemp = self.generator.newTemp()
                nuevoValor = Value(newtemp,True,tipoExpresion.BOOL)

                if self.trueLabel == "":
                    self.trueLabel = self.generator.newLabel()

                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()

                #Se crean temporales para almacenar las posiciones
                nuevoTmp1 = self.generator.newTemp()
                nuevoTmp2 = self.generator.newTemp()
                #tmp1 = valorIzq
                self.generator.addAsig(nuevoTmp1,izqValor.getValue())
                #tmp2 = valorDercha
                self.generator.addAsig(nuevoTmp2,drhValor.getValue())

                LabelFinCadena = self.generator.newLabel()
                LabelCiclo = self.generator.newLabel()

                tmpAlm1 = self.generator.newTemp()
                tmpAlm2 = self.generator.newTemp()

                self.generator.addLabel(LabelCiclo)
                self.generator.addGetHeap(tmpAlm1, nuevoTmp1)
                self.generator.addGetHeap(tmpAlm2, nuevoTmp2)

                self.generator.addIf(tmpAlm1,"-1","==",LabelFinCadena)
                self.generator.addIf(tmpAlm2,"-1","==",LabelFinCadena)

                self.generator.addIf(tmpAlm1,tmpAlm2,"!=",self.falseLabel)

                self.generator.addExpression(nuevoTmp1,nuevoTmp1,"1","+")
                self.generator.addExpression(nuevoTmp2,nuevoTmp2,"1","+")
                self.generator.addGoto(LabelCiclo)

                self.generator.addLabel(LabelFinCadena)
                self.generator.addIf(tmpAlm1,tmpAlm2,"==",self.trueLabel)
                self.generator.addGoto(self.falseLabel)

                nuevoValor.trueLabel = self.trueLabel
                nuevoValor.falseLabel = self.falseLabel

                newLabel = self.generator.newLabel()
                
                self.generator.addLabel(nuevoValor.trueLabel)
                self.generator.addAsig(newtemp,"1")

                self.generator.addGoto(newLabel)
                self.generator.addLabel(nuevoValor.falseLabel)
                self.generator.addAsig(newtemp,"0")

                self.generator.addLabel(newLabel)
                return nuevoValor
        
        
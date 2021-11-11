from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Instrucciones.SentenciasDeTransferencia.Return import Return
from Instrucciones.SentenciasDeTransferencia.Break import Break
from Instrucciones.SentenciasDeTransferencia.Continue import Continue
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class ElseIf(Instruction):

    def __init__(self, condicion, codigo,bloquesElseIf) -> None:
        super().__init__()
        self.condicion = condicion
        self.codigo = codigo
        self.bloquesElseIf = bloquesElseIf

    def compile(self, entorno: Environment) -> Value:
        self.condicion.generator = self.generator

        newLabel = self.generator.newLabel()

        valCondicion = self.condicion.compile(entorno)
        trueNewLabel = self.generator.newLabel()
        falseLabel = self.generator.newLabel()

        self.generator.addIf(valCondicion.value,"0","==",falseLabel)
        self.generator.addGoto(trueNewLabel)
        if (valCondicion.type == tipoExpresion.BOOL):
            self.generator.addLabel(trueNewLabel)

            

            for ins in self.codigo:
                ins.generator = self.generator
                if isinstance(ins,Break) :
                    ins.label = self.break_

                if isinstance(ins,Continue) :
                    ins.label = self.continue_

                if isinstance(ins,Return) :
                    ins.labelReturn = self.return_
                    ins.compile(entorno)
                    self.returnif = ins.hayreturn
                    continue
                ins.compile(entorno)

            self.generator.addGoto(newLabel)
            self.generator.addLabel(falseLabel)
            
        for instrucciones in self.bloquesElseIf:
            instrucciones[0].generator = self.generator
            valCondicion = instrucciones[0].compile(entorno)
            trueNewLabel = self.generator.newLabel()
            falseLabel = self.generator.newLabel()

            self.generator.addIf(valCondicion.value,"0","==",falseLabel)
            self.generator.addGoto(trueNewLabel)
            if (valCondicion.type == tipoExpresion.BOOL):
                self.generator.addLabel(trueNewLabel)

                

                for ins in instrucciones[1]:
                    ins.generator = self.generator
                    if isinstance(ins,Break) :
                        ins.label = self.break_

                    if isinstance(ins,Continue) :
                        ins.label = self.continue_

                    if isinstance(ins,Return) :
                        ins.labelReturn = self.return_
                        ins.compile(entorno)
                        self.returnif = ins.hayreturn
                        continue
                    ins.compile(entorno)

                self.generator.addGoto(newLabel)
                self.generator.addLabel(falseLabel)


        self.generator.addLabel(newLabel)
        return super().compile(entorno)

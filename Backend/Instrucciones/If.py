from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Instrucciones.SentenciasDeTransferencia.Continue import Continue
from Instrucciones.SentenciasDeTransferencia.Break import Break
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class If(Instruction):

    def __init__(self, condicion, codigo) -> None:
        super().__init__()
        self.condicion = condicion
        self.codigo = codigo
        self.break_ = ""
        self.continue_ = ""
        self.return_ = ""

    def compile(self, entorno: Environment) -> Value:
        self.condicion.generator = self.generator

        newLabel = self.generator.newLabel()

        valCondicion = self.condicion.compile(entorno)
        trueNewLabel = self.generator.newLabel()
        

        self.generator.addIf(valCondicion.value,"0","==",newLabel)
        self.generator.addGoto(trueNewLabel)
        if (valCondicion.type == tipoExpresion.BOOL):
            self.generator.addLabel(trueNewLabel)

            for ins in self.codigo:
                
                if isinstance(ins,Break) :
                    ins.label = self.break_

                if isinstance(ins,Continue) :
                    ins.label = self.continue_
                ins.generator = self.generator
                ins.compile(entorno)

            self.generator.addGoto(newLabel)

            self.generator.addLabel(newLabel)
        
        return super().compile(entorno)

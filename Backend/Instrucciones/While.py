from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class While(Instruction):

    def __init__(self, condicion, codigo) -> None:
        super().__init__()
        self.condicion = condicion
        self.codigo = codigo

    def compile(self, entorno: Environment) -> Value:
        self.condicion.generator = self.generator

        newLabel = self.generator.newLabel()

        
        self.generator.addLabel(newLabel)


        valCondicion = self.condicion.compile(entorno)
        trueNewLabel = self.generator.newLabel()
        falseNewLabel = self.generator.newLabel()

        self.generator.addIf(valCondicion.value,"0","==",falseNewLabel)
        self.generator.addGoto(trueNewLabel)
        if (valCondicion.type == tipoExpresion.BOOL):
            self.generator.addLabel(trueNewLabel)

            newEntorno = Environment(entorno,"ciclo")

            for ins in self.codigo:
                ins.generator = self.generator
                ins.compile(newEntorno)

            self.generator.addGoto(newLabel)

            self.generator.addLabel(falseNewLabel)
        
        return super().compile(entorno)

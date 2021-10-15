from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class PrinLn(Instruction):

    def __init__(self,lista) -> None:
        super().__init__()
        self.lista = lista

    def compile(self, entorno: Environment) -> Value:
        for exp in self.lista:
            exp.generator = self.generator

            tmp: Value = exp.compile(entorno)

            if tmp.type == tipoExpresion.INTEGER:
                self.generator.addPrintf("d","int("+str(tmp.getValue())+")")
            elif tmp.type == tipoExpresion.FLOAT:
                self.generator.addPrintf("f"," "+str(tmp.getValue()))
            elif tmp.type == tipoExpresion.STRING or tmp.type == tipoExpresion.CHAR:
                self.generator.addPrintfString("c",str(tmp.getValue()))
            else:
                print("Error en la print")

        
        self.generator.addNewLine()
        #return super().compile(entorno)
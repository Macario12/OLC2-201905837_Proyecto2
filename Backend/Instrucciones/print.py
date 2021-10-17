from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Print(Instruction):

    def __init__(self,exp:Expresion) -> None:
        super().__init__()
        self.exp = exp

    def compile(self, entorno: Environment) -> Value:

        self.exp.generator = self.generator

        tmp: Value = self.exp.compile(entorno)

        if tmp.type == tipoExpresion.INTEGER:
            self.generator.addPrintf("d","int("+str(tmp.getValue())+")")
        elif tmp.type == tipoExpresion.FLOAT:
            self.generator.addPrintf("f",str(tmp.getValue()))
        elif tmp.type == tipoExpresion.STRING or tmp.type == tipoExpresion.CHAR:
            self.generator.addPrintfString("c",str(tmp.getValue()))
        elif tmp.type == tipoExpresion.BOOL:
            newLabel = self.generator.newLabel()
            newLabel2 = self.generator.newLabel()
            newLabel3 = self.generator.newLabel()

            self.generator.addIf(tmp.getValue(),"1","!=",newLabel2)
            self.generator.addGoto(newLabel)
            self.generator.addLabel(newLabel)
            self.generator.addCallFunc("print_true")
            self.generator.addGoto(newLabel3)

            
            self.generator.addLabel(newLabel2)
            self.generator.addCallFunc("print_false")

            self.generator.addLabel(newLabel3)

        else:
            print("Error en la print")

        
        #return super().compile(entorno)
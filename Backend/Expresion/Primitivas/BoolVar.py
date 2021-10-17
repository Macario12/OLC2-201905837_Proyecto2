from Abstract.Expresion import Expresion
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class BoolVal(Expresion):
    def __init__(self,tipo:tipoExpresion, valor) -> None:
        super().__init__()
        self.tipo = tipo
        self.valor = valor

    def compile(self, entorno: Environment) -> Value:

        try:

            if self.tipo == tipoExpresion.BOOL:
                return Value(str(self.valor),False,self.tipo)

        except:
            print('No se reconoce el valor')
            return Value("0",False,tipoExpresion.BOOL)
    
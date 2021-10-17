from os import terminal_size
from Abstract.Expresion import Expresion
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion
class Identificador(Expresion):
    def __init__(self,id) -> None:
        super().__init__()
        self.id  = id

    def compile(self, entorno: Environment) -> Value:

        try:
            varSimbolo = entorno.getVariable(self.id)
            nuevoTemp = self.generator.newTemp()
            self.generator.addGetStack(nuevoTemp,str(varSimbolo.position))
            return Value(str(nuevoTemp),True,varSimbolo.type)
        except:
            print('No se reconoce el valor')
            return Value("0",False,tipoExpresion.BOOL)
    
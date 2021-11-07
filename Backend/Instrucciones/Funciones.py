from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Instrucciones.SentenciasDeTransferencia.Return import Return
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion

class Function(Instruction):

    def __init__(self, id,parametros, codigo,tipoFuncion) -> None:
        super().__init__()
        self.id = id
        self.parametros = parametros
        self.codigo = codigo
        self.tipo = tipoFuncion

    def compile(self, entorno: Environment) -> Value:
        #Para guardarlo en el vector de funciones;
        self.generator.inFuncion = True
        #Se crea un entorno Nuevo para las funciones.
        newEntorno = Environment(entorno)
        #Se asigna el cambio de tamaños
        sizeTablaGen = newEntorno.size
        newEntorno.size = newEntorno.sizeEntornoActual
        self.generator.addFunction(self.id)
        
        #Hay return
        hayreturn = False;
        labelreturn = self.generator.newLabel()

        if self.parametros != None:
            for parametro in self.parametros:
                newEntorno.saveVariable(parametro[0],parametro[1])
        
        #Recorremos el arreglo del codigo para ejecutar el codigo
        for ins in self.codigo:
            ins.generator = self.generator
            if isinstance(ins,Return):
                #obtenes la expresion del return
                hayreturn = True
                expresionReturn = ins.compile(newEntorno)
                tempReturn = ins.generator.newTemp()
                ins.generator.addComentario("Return")
                ins.generator.addExpression(tempReturn,"P","0","+")
                ins.generator.addSetStack(tempReturn,expresionReturn.getValue())
                ins.generator.addGoto(labelreturn)
                continue

            ins.compile(newEntorno)

        
        if(hayreturn):
            self.generator.addLabel(labelreturn)
        
        self.generator.addReturn()
        self.generator.addllaveC()
        #Almacenamos la funcion.
        entorno.saveFunction(self.id,newEntorno.size,self.tipo)

        #Asignando el tamaño de la tabla anterior
        newEntorno.size = sizeTablaGen
        self.generator.inFuncion = False
        return super().compile(entorno)

            
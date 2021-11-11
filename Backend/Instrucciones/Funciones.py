from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Instrucciones.IfElse import IfElse
from Instrucciones.ElseIf import ElseIf
from Instrucciones.ElseIfElse import ElseIfElse
from Instrucciones.If import If
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
        self.generator.addComentario("Inicio Funcion")
        #Se crea un entorno Nuevo para las funciones.
        newEntorno = Environment(entorno,"funcion")
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
                ins.labelReturn =labelreturn
                ins.compile(newEntorno)
                hayreturn = ins.hayreturn
                continue

            if isinstance(ins,If):
                #obtenes la expresion del return
                ins.return_ =labelreturn
                ins.compile(newEntorno)
                hayreturn = ins.returnif
                continue

            if isinstance(ins,IfElse):
                #obtenes la expresion del return
                ins.return_ =labelreturn
                ins.compile(newEntorno)
                hayreturn = ins.returnif
                continue
            
            if isinstance(ins,ElseIf):
                #obtenes la expresion del return
                ins.return_ =labelreturn
                ins.compile(newEntorno)
                hayreturn = ins.returnif
                continue

            if isinstance(ins,ElseIfElse):
                #obtenes la expresion del return
                ins.return_ =labelreturn
                ins.compile(newEntorno)
                hayreturn = ins.returnif
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
        self.generator.addComentario("Fin Funcion")
        self.generator.inFuncion = False
        return super().compile(entorno)

            
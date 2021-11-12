from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Entorno.Simbolo import Simbolo
from Instrucciones.ElseIf import ElseIf
from Instrucciones.IfElse import IfElse
from Instrucciones.ElseIfElse import ElseIfElse
from Instrucciones.If import If
from Instrucciones.SentenciasDeTransferencia.Break import Break
from Expresion.Primitivas.NumberVal import NumberVal
from Expresion.Aritmeticas.Suma import Suma
from Expresion.Aritmeticas.Resta import Resta
from Expresion.Primitivas.Identificador import Identificador
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion
from Expresion.Relacionales.Menor import Menor
from Instrucciones.AsignacionD import Asignacion

class ForExpresion(Instruction):

    def __init__(self, id,expresion:Expresion, codigo) -> None:
        super().__init__()
        self.id = id
        self.expresion = expresion
        self.codigo = codigo

    def compile(self, entorno: Environment) -> Value:
        
        self.expresion.generator = self.generator
        indice = self.expresion.compile(entorno)

        self.generator.addComentario("Ciclo For Expresiones")
        #Se debe de crear un nuevo entorno 
        nuevoEntnorFor = Environment(entorno,"ciclo")
        
        temporalItem = self.generator.newTemp()
        #Se crea la temporal
        self.generator.addExpression(temporalItem,indice.getValue(),"1","-")
        
        
        #se crea temporal para aumentar
        #temporalAumento = self.generator.newTemp()
        #creamos nuevo Label para el ciclo
        newLabel = self.generator.newLabel()
        
        #Creamos Etiquetas False and True para validar la condicion
        trueNewLabel = self.generator.newLabel()
        falseNewLabel = self.generator.newLabel()

        #agregamoss Label para enciclar 
        self.generator.addLabel(newLabel)
        
        #Incrementamos en 1 la variable
        self.generator.addExpression(temporalItem,temporalItem,"1","+")
        temporalAcceso = self.generator.newTemp()
        self.generator.addGetHeap(temporalAcceso,temporalItem)
        
        tempVar: Simbolo = nuevoEntnorFor.saveVariable(self.id,tipoExpresion.CHAR)
        temporalAsignacion = self.generator.newTemp()
        self.generator.addExpression(temporalAsignacion,"P",str(tempVar.position),"+")
        self.generator.addSetStack(temporalAsignacion, temporalAcceso)
        
        #Agregamos If para validar el valor booleano
        self.generator.addIf(temporalAcceso,"-1","==",falseNewLabel)
        self.generator.addGoto(trueNewLabel)
        
        self.generator.addLabel(trueNewLabel)
        #Creamos un entorno nuevo para el for. 
        newEntorno = Environment(nuevoEntnorFor,"ciclo")
        #Ejecutamos el bloque de codigo que se encicla
        for ins in self.codigo:
            
            if isinstance(ins,If):
                ins.break_ = falseNewLabel
                ins.continue_ = newLabel
            
            if isinstance(ins,IfElse):
                ins.break_ = falseNewLabel
                ins.continue_ = newLabel
            
            if isinstance(ins,ElseIf):
                ins.break_ = falseNewLabel
                ins.continue_ = newLabel

            if isinstance(ins,ElseIfElse):
                ins.break_ = falseNewLabel
                ins.continue_ = newLabel

            

            ins.generator = self.generator
            ins.compile(newEntorno)

        

        #Agregamos goto para seguir el ciclo.
        self.generator.addGoto(newLabel)
        #Agregamos etiqueta para La siguiente Instruccion.
        self.generator.addLabel(falseNewLabel)
        
        return super().compile(entorno)

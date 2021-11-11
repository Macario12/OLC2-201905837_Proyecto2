from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
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

class For(Instruction):

    def __init__(self, id,inicio,final, codigo) -> None:
        super().__init__()
        self.id = id
        self.inicio = inicio
        self.final = final
        self.codigo = codigo

    def compile(self, entorno: Environment) -> Value:
        
        self.generator.addComentario("Ciclo For")
        #Se debe de crear un nuevo entorno 
        nuevoEntnorFor = Environment(entorno,"ciclo")
        #Se crea la Variable
        decre = Resta(self.inicio,NumberVal(tipoExpresion.INTEGER,1))
        tmpVar = Asignacion(self.id,decre,None)
        tmpVar.generator = self.generator
        tmpVar.compile(nuevoEntnorFor)
        #Se manda a buscar la variable para pasarla a la condicion.
        var = Identificador(self.id)

        

        #creamos nuevo Label para el ciclo
        newLabel = self.generator.newLabel()

        #Creamos Label para enciclar 
        self.generator.addLabel(newLabel)
        #Se crea la condicion para el ciclo y se compila
        condicion = Menor(var,self.final)
        condicion.generator = self.generator
        valCondicion = condicion.compile(nuevoEntnorFor)
        #Creamos Etiquetas False and True para validar la condicion
        trueNewLabel = self.generator.newLabel()
        falseNewLabel = self.generator.newLabel()
        
        #Incrementamos en 1 la variable
        incremento = Suma(var,NumberVal(tipoExpresion.INTEGER,1))
        tmpVar = Asignacion(self.id,incremento,None)
        tmpVar.generator = self.generator
        tmpVar.compile(nuevoEntnorFor)
        
        #Agregamos If para validar el valor booleano
        self.generator.addIf(valCondicion.value,"0","==",falseNewLabel)
        self.generator.addGoto(trueNewLabel)
        
        


        if (valCondicion.type == tipoExpresion.BOOL):
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

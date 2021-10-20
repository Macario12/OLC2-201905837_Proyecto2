from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruction
from Expresion.Primitivas.NumberVal import NumberVal
from Expresion.Aritmeticas.Suma import Suma
from Expresion.Primitivas.Identificador import Identificador
from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Enum.tipoExpresion import tipoExpresion
from Expresion.Relacionales.MenorIgual import MenorIgual
from Instrucciones.AsignacionD import Asignacion

class For(Instruction):

    def __init__(self, id,inicio,final, codigo) -> None:
        super().__init__()
        self.id = id
        self.inicio = inicio
        self.final = final
        self.codigo = codigo

    def compile(self, entorno: Environment) -> Value:
        

        #Se debe de crear un nuevo entorno 
        nuevoEntnorFor = Environment(entorno)
        #Se crea la Variable
        tmpVar = Asignacion(self.id,self.inicio)
        tmpVar.generator = self.generator
        tmpVar.compile(nuevoEntnorFor)
        #Se manda a buscar la variable para pasarla a la condicion.
        var = Identificador(self.id)


        #creamos nuevo Label para el ciclo
        newLabel = self.generator.newLabel()

        #Creamos Label para enciclar 
        self.generator.addLabel(newLabel)
        #Se crea la condicion para el ciclo y se compila
        condicion = MenorIgual(var,self.final)
        condicion.generator = self.generator
        valCondicion = condicion.compile(nuevoEntnorFor)
        #Creamos Etiquetas False and True para validar la condicion
        trueNewLabel = self.generator.newLabel()
        falseNewLabel = self.generator.newLabel()
        #Agregamos If para validar el valor booleano
        self.generator.addIf(valCondicion.value,"0","==",falseNewLabel)
        self.generator.addGoto(trueNewLabel)
        if (valCondicion.type == tipoExpresion.BOOL):
            self.generator.addLabel(trueNewLabel)
            #Creamos un entorno nuevo para el for. 
            newEntorno = Environment(nuevoEntnorFor)
            #Ejecutamos el bloque de codigo que se encicla
            for ins in self.codigo:
                ins.generator = self.generator
                ins.compile(newEntorno)

            #Incrementamos en 1 la variable
            incremento = Suma(var,NumberVal(tipoExpresion.INTEGER,1))
            tmpVar = Asignacion(self.id,incremento)
            tmpVar.generator = self.generator
            tmpVar.compile(nuevoEntnorFor)


            #Agregamos goto para seguir el ciclo.
            self.generator.addGoto(newLabel)
            #Agregamos etiqueta para La siguiente Instruccion.
            self.generator.addLabel(falseNewLabel)
        
        return super().compile(entorno)

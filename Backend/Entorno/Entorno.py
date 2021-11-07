from Enum.tipoExpresion import tipoExpresion
from Entorno.Simbolo import Simbolo

class Environment:

    def __init__(self, father) -> None:
        self.father = father
        self.variable = {}
        self.funciones = {}
        self.size = 0
        self.sizeEntornoActual = 1

        if(father != None):
            self.size = father.size
        

    def saveVariable(self, id: str, type: tipoExpresion):
        if (self.variable.get(id) != None):
            print("La variable " + id + " ya existe")
            return

        tempVar = Simbolo(id,type,str(self.size))
        self.size = self.size + 1
        self.sizeEntornoActual = self.sizeEntornoActual +1
        self.variable[id] = tempVar
        return tempVar

    def getVariable(self, id: str) -> Simbolo:
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.variable.get(id) != None):
                return tempEnv.variable.get(id)
            tempEnv = tempEnv.father
        #print("Error: la variable " + id + " no existe")
        return None

    #devuelve el entorno Global
    def getEntornoGlobal(self):
        tempEntorno = self
        contador = 0
        while tempEntorno != None:
            contador += 1
            tempEntorno = tempEntorno.father
        contador1 = 0
        entornGlobal = self
        while contador1 < contador-1:
            contador1 += 1
            entornGlobal = entornGlobal.father

        return entornGlobal
    
    def updateVariable(self, id: str,type:tipoExpresion) -> Simbolo:
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.variable.get(id) != None):
                tmpVar = Simbolo(id,type,tempEnv.variable.get(id).position)
                tempEnv.variable[id] = tmpVar

                return tmpVar
            tempEnv = tempEnv.father
        #print("Error: la variable " + id + " no existe")
        return None

    
    def existeVariableEntornoActual(self,id):
        tempEntorno = self
        while tempEntorno != None:
            if tempEntorno.variable.get(id) != None:
                return False
            return True 

    #FUNCIONES

    def saveFunction(self, id: str,size:int,tipo):
        if (self.funciones.get(id) != None):
            print("La variable " + id + " ya existe")
            return

        tempVar = Simbolo(id,tipo,str(size))
        self.funciones[id] = tempVar
        

    def getFunction(self, id: str) -> Simbolo:
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.funciones.get(id) != None):
                return tempEnv.funciones.get(id)
            tempEnv = tempEnv.father
        #print("Error: la variable " + id + " no existe")
        return None
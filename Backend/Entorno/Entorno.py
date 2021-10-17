from Enum.tipoExpresion import tipoExpresion
from Entorno.Simbolo import Simbolo

class Environment:

    def __init__(self, father) -> None:
        self.father = father
        self.variable = {}
        self.size = 0

        if(father != None):
            self.size = father.size
        

    def saveVariable(self, id: str, type: tipoExpresion):
        if (self.variable.get(id) != None):
            print("La variable " + id + " ya existe")
            return

        tempVar = Simbolo(id,type,str(self.size))
        self.size = self.size + 1
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
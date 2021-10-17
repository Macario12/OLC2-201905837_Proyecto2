class Generator:
    def __init__(self) -> None:
        self.generator = None
        self.temporal = 0
        self.label = 0
        self.code = []
        self.tempList = []

    #Obtener los temporales usados
    def getUsedTemps(self) -> str:
        return ",".join(self.tempList)

    #Obtener el codigo generado
    def getCode(self) -> str:
        tempCode: str = 'package main \n'
        #tempCode = tempCode + 'import (\"fmt\"\n\"math\") \n'
        tempCode = tempCode + 'import (\"fmt\") \n'
        tempCode = tempCode + 'var stack[10000000]float64;\n'
        tempCode = tempCode + 'var heap[10000000]float64;\n'
        tempCode = tempCode + 'var P,H float64;'
        
        if (len(self.tempList)>0):
            tempCode = tempCode + "\nvar "+self.getUsedTemps()+" float64; \n\n"

        tempCode = tempCode + '\nfunc print_false(){\n'
        tempCode = tempCode + "\n fmt.Printf(\"%c\",102);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",97);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",108);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",115);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",101);"
        tempCode = tempCode + '\n}\n'

        tempCode = tempCode + '\nfunc print_true(){\n'
        tempCode = tempCode + "\n fmt.Printf(\"%c\",116);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",114);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",117);"
        tempCode = tempCode + "\n fmt.Printf(\"%c\",101);"
        tempCode = tempCode + '\n}\n'

        
        tempCode = tempCode + '\nfunc main(){\n'
        tempCode = tempCode + "\n".join(self.code)
        tempCode = tempCode + '\n}\n'
        
        return tempCode

    def newTemp(self)-> str:
        temp = "t"+str(self.temporal)
        self.temporal = self.temporal +1
        
        self.tempList.append(temp)

        return temp
    
    def newLabel(self) -> str:
        temp = self.label
        self.label = self.label + 1
        return "L" + str(temp)

    def addCallFunc(self, name: str):
        self.code.append(name + "();")

    #Añade label al codigo
    def addLabel(self, label: str):
        self.code.append(label + ":")

    def addExpression(self, target: str, left: str, right: str, operator: str):
        self.code.append(target + " = " + left + " " + operator + " " + right + ";")
    
    def addAsig(self, target: str, left: str):
        self.code.append(target + " = " + left +";")

    def addModulo(self, target: str, left: str, right: str):
        self.code.append(target + " = math.Mod(" + left + ","+right + ");")

    def addIf(self, left: str, rigth: str, operator: str, label: str):
        self.code.append("if(" + left + " " + operator + " " + rigth + "){ goto " + label + ";}")

    def addGoto(self, label:str):
        self.code.append("goto " + label + ";")

    #Añade un printf
    def addPrintfString(self, typePrint:str, value:str):
        for character in value:
            self.code.append("fmt.Printf(\"%" + typePrint + "\"," + str(ord(character)) + ");")

    def addPrintf(self, typePrint:str, value:str):
        self.code.append("fmt.Printf(\"%" + typePrint + "\"," + value + ");")

    #Salto de linea
    def addNewLine(self):
        self.code.append('fmt.Printf(\"%c\",10);')

    #Se mueve hacia la posicion siguiente del heap
    def addNextHeap(self):
            self.code.append("H = H + 1;")
    
    #Se mueve hacia la posicion siguiente del stack
    def addNextStack(self,index:str):
        self.code.append("P = P + " + index + ";")
    

    #Se mueve hacia la posicion anterior del stack
    def addBackStack(self, index:str):
            self.code.append("P = P - " + index + ";")

    #Obtiene el valor del heap en cierta posicion
    def addGetHeap(self, target:str, index: str):
        self.code.append(target + " = HEAP[(int)" + index + " ];")

    #Inserta valor en el heap
    def addSetHeap(self, index:str, value:str):
        self.code.append("HEAP[(int)" + index + "] = " + value + ";" )
    

    #Obtiene valor del stack en cierta posicion
    def addGetStack(self,target:str, index:str):
        self.code.append(target + " = stack[int(" + index + ")];")

    #INserta valor al stack
    def addSetStack(self, index:str, value:str):
        self.code.append("stack[int(" + index + ")] = " + value + ";" )
    
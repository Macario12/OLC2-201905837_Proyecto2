

class Generator:
    def __init__(self) -> None:
        self.generator = None
        self.temporal = 6
        self.label = 4
        self.code = []
        self.funcioncode = []
        self.NativeCode = []
        self.tempList = []
        self.inFuncion = False
        self.inNatives = False

    #Obtener los temporales usados
    def getUsedTemps(self) -> str:
        return ",".join(self.tempList)

    #Obtener el codigo generado
    def getCode(self) -> str:
        tempCode: str = 'package main \n'
        #tempCode = tempCode + 'import (\"fmt\"\n\"math\") \n'
        tempCode = tempCode + 'import (\"fmt\") \n'
        tempCode = tempCode + 'var stack[30101999]float64;\n'
        tempCode = tempCode + 'var heap[30101999]float64;\n'
        tempCode = tempCode + 'var P,H float64;'
        
        if (len(self.tempList)>0):
            tempCode = tempCode + "\nvar t0,t1,t2,t3,t4,t5,"+self.getUsedTemps()+" float64; \n\n"

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
        
        self.printString()
        self.concatenarStrings()

        tempCode = tempCode + "\n".join(self.NativeCode)

        tempCode = tempCode + "\n".join(self.funcioncode)

        tempCode = tempCode + '\nfunc main(){\n'
        tempCode = tempCode + "\n".join(self.code)
        tempCode = tempCode + '\n}\n'
        
        return tempCode

    def codeIn(self, code):
        if(self.inNatives):
            self.NativeCode.append(code);
            
        elif(self.inFuncion):
            self.funcioncode.append(code)
            
        else:
            self.code.append(code)

    def printString(self):
        self.NativeCode.append("func printString(){")
        self.NativeCode.append("t0"+"="+"P;")
        self.NativeCode.append("t1 ="+"t0;")
        self.NativeCode.append("L0"+":")
        self.NativeCode.append("t2"+"= heap[int("+"t1"+")];")
        self.NativeCode.append("if "+ "t2"+"=="+"-1{ goto "+"L1"+";}")
        self.NativeCode.append("fmt.Printf(\"%c\", int("+"t2"+"));")
        self.NativeCode.append("t1" +"="+"t1"+"+1;")
        self.NativeCode.append("goto "+"L0"+";")
        self.NativeCode.append("L1"+":")
        
        self.NativeCode.append("return;")
        self.NativeCode.append("}")

    def concatenarStrings(self):
        self.NativeCode.append("func concatenarStrings(){")
        self.NativeCode.append("t3"+"="+"P;")
        self.NativeCode.append("t4 ="+"t3;")
        self.NativeCode.append("L2"+":")
        self.NativeCode.append("t5"+"= heap[int("+"t4"+")];")
        self.NativeCode.append("if "+ "t5"+"=="+"-1{ goto "+"L3"+";}")
        self.NativeCode.append("heap[int(H)] = t5;")
        self.NativeCode.append("H = H +1;")
        self.NativeCode.append("t4" +"="+"t4"+"+1;")
        self.NativeCode.append("goto "+"L2"+";")
        self.NativeCode.append("L3"+":")
        
        self.NativeCode.append("return;")
        self.NativeCode.append("}")

    def addFunction(self, nombre: str):
        self.codeIn("\nfunc "+ nombre+"(){")
    def addllaveC(self):
        self.codeIn("}")
    
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
        self.codeIn(name + "();")

    def addComentario(self, comentario: str):
        self.codeIn("/*"+comentario + "*/")

    def addReturn(self):
        self.codeIn("return;")

    #Añade label al codigo
    def addLabel(self, label: str):
        self.codeIn(label + ":")

    def addExpression(self, target: str, left: str, right: str, operator: str):
        self.codeIn(target + " = " + left + " " + operator + " " + right + ";")
    
    def addAsig(self, target: str, left: str):
        self.codeIn(target + " = " + left +";")

    def addModulo(self, target: str, left: str, right: str):
        self.codeIn(target + " = math.Mod(" + left + ","+right + ");")

    def addIf(self, left: str, rigth: str, operator: str, label: str):
        self.codeIn("if(" + left + " " + operator + " " + rigth + "){ goto " + label + ";}")

    def addGoto(self, label:str):
        self.codeIn("goto " + label + ";")

    #Añade un printf
    def addPrintfString(self, typePrint:str, value:str):
        for character in value:
            self.codeIn("fmt.Printf(\"%" + typePrint + "\"," + str(ord(character)) + ");")

    def addPrintf(self, typePrint:str, value:str):
        self.codeIn("fmt.Printf(\"%" + typePrint + "\"," + value + ");")

    #Salto de linea
    def addNewLine(self):
        self.codeIn('fmt.Printf(\"%c\",10);')

    #Se mueve hacia la posicion siguiente del heap
    def addNextHeap(self):
        self.codeIn("H = H + 1;")
    
    #Se mueve hacia la posicion siguiente del stack
    def addNextStack(self,index:str):
        self.codeIn("P = P + " + index + ";")
    

    #Se mueve hacia la posicion anterior del stack
    def addBackStack(self, index:str):
        self.codeIn("P = P - " + index + ";")

    #Obtiene el valor del heap en cierta posicion
    def addGetHeap(self, target:str, index: str):
        self.codeIn(target + " = heap[int(" + index + ")];")

    #Inserta valor en el heap
    def addSetHeap(self, index:str, value:str):
        self.codeIn("heap[int(" + index + ")] = " + value + ";" )
    

    #Obtiene valor del stack en cierta posicion
    def addGetStack(self,target:str, index:str):
        self.codeIn(target + " = stack[int(" + index + ")];")

    #INserta valor al stack
    def addSetStack(self, index:str, value:str):
        self.codeIn("stack[int(" + index + ")] = " + value + ";" )
    
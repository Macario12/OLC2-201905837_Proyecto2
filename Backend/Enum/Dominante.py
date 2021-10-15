from Enums.tipoExpresion import tipoExpresion

def Dominante(izq:tipoExpresion,der:tipoExpresion)->tipoExpresion:
        if izq == 'STRING' and der == 'STRING':
                return tipoExpresion.STRING
        elif izq == 'STRING' and der == 'INTEGER':
                return tipoExpresion.STRING
        elif izq == 'STRING' and der =='FLOAT':
                return tipoExpresion.STRING
        elif izq == 'INTEGER' and der == 'STRING':
                return tipoExpresion.STRING
        elif izq == 'FLOAT' and der == 'STRING':
                return tipoExpresion.STRING
        elif izq == 'INTEGER' and der == 'INTEGER':
                return tipoExpresion.INTEGER
        elif izq == 'INTEGER' and der == 'FLOAT':
                return tipoExpresion.FLOAT
        elif izq == 'FLOAT' and der == 'INTEGER':
                return tipoExpresion.FLOAT
        elif izq == 'FLOAT' and der == 'FLOAT':
                return tipoExpresion.FLOAT
        elif izq == 'BOOL' and der == 'BOOL' :
                return tipoExpresion.BOOL
        elif izq == 'INTEGER':
                return tipoExpresion.INTEGER
        elif izq == 'FLOAT':
                return tipoExpresion.FLOAT
        elif izq == 'STRING':
                return tipoExpresion.STRING
        elif izq == 'BOOL':
                return tipoExpresion.BOOL
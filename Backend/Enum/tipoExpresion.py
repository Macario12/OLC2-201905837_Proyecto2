import enum

class tipoExpresion(enum.Enum):
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    BOOL = 'BOOL'
    CHAR = 'CHAR'
    IDENTIFICADOR = 'IDENTIFICADOR'
    ARREGLO = 'ARREGLO'
    NULO = 'NOTHING'
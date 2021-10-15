import enum

class tipoNativa(enum.Enum):
    LOG10 = 'LOG10'
    LOG = 'LOG'
    SIN = 'SIN'
    COS = 'COS'
    TAN = 'TAN'
    SQRT = 'SQRT'
    PARSE = 'PARSE'
    TRUNC = 'TRUNC'
    FLOAT = 'FLOAT'
    STRING = 'STRING'
    TYPEOF = 'TYPEOF'
    UPPERCASE ='UPPERCASE'
    LOWERCASE = 'LOWERCASE'

    #ARREGLOS
    PUSH = 'PUSH'
    POP = 'POP'
    LENGTH = 'LENGTH'
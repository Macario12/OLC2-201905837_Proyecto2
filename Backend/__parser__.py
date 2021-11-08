'''from Instrucion.AsignacionArreglo import AsignacionArreglo
from Instrucion.AccesoArreglo import AccesoArray
from Instrucion.nativasArreglo import NativasArray
from Expresiones.Arreglo import Arreglo
from Expresiones.Function import Func
from Instrucion.tranferencia import transferencia
from Enums.tipoTranferencia import tipoTransferencia
from Instrucion.For2 import ForS
from Instrucion.For import For
from Instrucion.CicloWhile import CicloWhile
from Instrucion.ElseIf import ElseIf
from Instrucion.IfElse import IfElse
from Instrucion.If import If
from Enums.tipoEntorno import tipoEntorno
from Entorno.Simbolo import Simbolo
from Instrucion.llamadaFunc import LlamadaFunc
from Instrucion.Dec_Funcion import DecFuncion
from Errores.Excepcion import Excepcion'''
errores = []

reserved = {
    'print' : 'PRINT',
    'println' : 'PRINTLN',
    
    'false' : 'FALSE',
    'true' : 'TRUE',
    
    'log10' : 'LOG10',
    'log' : 'LOG',
    'sin' : 'SIN',
    'cos' : 'COS',
    'tan' : 'TAN',
    'sqrt' : 'SQRT',

    'nothing' : 'NULL',
    
    'Int64' : 'INT',
    'Float64':'FLOAT',
    'Bool' :'BOOL',
    'Char' : 'CHAR',
    'String' : 'STRING',

    'local' : 'LOCAL',
    'global': 'GLOBAL',
    'function': 'FUNCTION',
    'end': 'END',
    'global': 'GLOBAL',
    'local': 'LOCAL',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE',
    'parse': 'PARSE',
    'trunc': 'TRUNC',
    'float': 'FLOAT_',

    'string': 'STRING_',
    'typeof': 'TYPEOF',
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'while': 'WHILE',
    'in': 'IN',
    'for': 'FOR',
    'return':'RETURN',
    'continue':'CONTINUE',
    'break':'BREAK',
    'pop': 'POP',
    'push': 'PUSH',
    'length': 'LENGTH'
}

tokens = [
    #OPERADORES
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    'PARENTESISABIERTO',
    'PARENTESISCERRADO',
    #RELACIONALES
    'MAYOR',
    'MENOR',
    'IGUAL',
    'IGUALIGUAL',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DIFERENTE',
    #LOGICAS
    'AND',
    'OR',
    'NOT',
    'PTCOMA',
    #EXPRESIONES
    'ID',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',
    #Reservadas
    'COMA',
    'DSPUNTOS',
    'CORCHETEA',
    'CORCHETEC',
    
] + list(reserved.values())

#ASIGNACION DE TOKENS

t_MAS = r'\+'
t_MENOS= r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_MODULO =r'%'
t_PARENTESISABIERTO =r'\('
t_PARENTESISCERRADO = r'\)'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_IGUALIGUAL=r'=='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_DIFERENTE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_DSPUNTOS = r':'
t_PTCOMA = r';'
t_COMA = r','
t_CORCHETEA = r'\['
t_CORCHETEC = r'\]'
#NATIVAS

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|.)?\'""" #creo que hay que mejorarla pq no reconoce dos caracteres como \n \t
    t.value = t.value[1:-1]
    return t

""" def t_ignore_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple # ...
def t_ignore_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1 """


def t_newline (t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")

def find_column(inp, token): #Documentacion PLY
     line_start = inp.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1


def t_error(t):
    _error = []
    _error.append("Error Lexico")
    _error.append(t.lexer.lineno)
    _error.append(find_column(inp, t))
    errores.append(_error)
    #print("hola")
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

#CARACTERES A IGNORAR
t_ignore = " \t\r"
t_ignore_COMMENT = r'\#.*'
t_ignore_COMMENTM = r'\#=(.|\n)*?=\#'

#Analizador Lexico
from Instrucciones.SentenciasDeTransferencia.Continue import Continue
from Instrucciones.SentenciasDeTransferencia.Break import Break
from Instrucciones.LlamadaFunciones import LLamadaFuncion
from Instrucciones.SentenciasDeTransferencia.Return import Return
from Instrucciones.Funciones import Function
from Expresion.Nativas.Strings import StringNative
from Instrucciones.For import For
from Instrucciones.ElseIfElse import ElseIfElse
from Instrucciones.ElseIf import ElseIf
from Instrucciones.IfElse import IfElse
from Instrucciones.If import If
from Expresion.Logicas.And import And
from Expresion.Logicas.Or import Or
from Expresion.Logicas.Not import Not
from Instrucciones.While import While
from Expresion.Primitivas.BoolVar import BoolVal
from Instrucciones.Declaracion import Declaracion
from Instrucciones.AsignacionD import Asignacion
from Expresion.Aritmeticas.Potencia import Potencia
from Expresion.Aritmeticas.Modulo import Modulo
from Expresion.Relacionales.MenorIgual import MenorIgual
from Expresion.Relacionales.MayorIgual import MayorIgual
from Expresion.Relacionales.IgualIgual import IgualIgual
from Expresion.Relacionales.Diferente import Diferente
from Expresion.Relacionales.Mayor import Mayor
from Expresion.Relacionales.Menor import Menor
from Expresion.Primitivas.TextVal import TextVal
from Expresion.Primitivas.Identificador import Identificador
from Instrucciones.println import PrinLn
from Expresion.Aritmeticas.RestaUnaria import RestaU
from Expresion.Aritmeticas.Resta import Resta
from Expresion.Aritmeticas.Division import Division
from Expresion.Aritmeticas.Multiplicacion import Multiplicacion
from Enum.tipoExpresion import tipoExpresion
from Expresion.Aritmeticas.Suma import Suma
from Expresion.Primitivas.NumberVal import NumberVal
from Instrucciones.print import Print
import ply.lex as lex

lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALIGUAL','DIFERENTE','MENOR','MAYOR','MAYORIGUAL','MENORIGUAL'),
    ('left', 'MAS','MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION','MODULO'),
    ('nonassoc', 'POTENCIA'),
    ('right', 'UMINUS'),
)

#DEFINICION DE GRAMATICA
start = 'initial'

def p_initial(t):
    'initial : instructions'
    t[0] = t[1]

def p_instruccion_error(p):
    'instruction : error PTCOMA'
    _errorS = []
    
    _errorS.append("Error Sintactico"+ str(p[1].value))
    _errorS.append(p.lineno(1))
    _errorS.append(find_column(inp, p.slice[1]))
    errores.append(_errorS)
    p[0] = ""


def p_instructions(t):
    'instructions : instructions instruction'
    if(t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]

def p_instructions_instruction(t):
    '''instructions :  instruction
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_cuerpoMetodo(t):
    'cuerpoFuncion : cuerpoFuncion instruction'
    if(t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]

def p_instructions_cuerpoFuncion(t):
    '''cuerpoFuncion :  instruction
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruction(t):
    '''instruction : impresion
                    | asignacion
                    | funcion
                    | llamadaFunc
                    | ifs
                    | whiles
                    | fors
                    | traferencia
                    | nativaArayPtC
    '''
    t[0] = t[1]

################################################################# FOR ##########################################################
def p_for(t):
    '''fors : FOR ID IN expresiones DSPUNTOS expresiones cuerpoFuncion END PTCOMA
            | FOR ID IN expresiones cuerpoFuncion END PTCOMA
    '''
    if len(t) == 10: t[0] = For(t[2],t[4],t[6],t[7])
    """if len(t) == 8: t[0] = ForS(t[2],t[4],t[5]) """
def p_impresion(t):
    '''impresion : PRINT PARENTESISABIERTO expresionescomma PARENTESISCERRADO PTCOMA
       | PRINTLN PARENTESISABIERTO expresionescomma PARENTESISCERRADO PTCOMA
    '''
    if t[1] == 'print' : t[0] = Print(t[3])
    elif t[1] == 'println': t[0] = PrinLn(t[3])

def p_impresion2(t):
    '''impresion : PRINTLN PARENTESISABIERTO PARENTESISCERRADO PTCOMA
    '''
    """ t[0] = Println(None) """

def p_impresiones_coma_lista(t):
    '''expresionescomma : expresionescomma COMA expresiones'''
    if(t[3] != ""):
        t[1].append(t[3])
    t[0] = t[1]

def p_impresiones_coma(t):
    '''expresionescomma :  expresiones
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_entornoType(t):
    '''entornoT : LOCAL
            | GLOBAL
    '''
    """ if t[1] == 'local' : t[0] = tipoEntorno.LOCAL
    elif t[1] == 'global': t[0] = tipoEntorno.GLOBAL """
########################################################## ASIGNACION DECLARACION ############################################
def p_asignacion(t):
    '''asignacion : ID IGUAL expresiones DSPUNTOS DSPUNTOS tipos PTCOMA
       |  ID IGUAL expresiones PTCOMA
       | entornoT ID IGUAL expresiones DSPUNTOS DSPUNTOS tipos PTCOMA
       | entornoT ID IGUAL expresiones PTCOMA
       | entornoT ID PTCOMA
     '''
    if len(t) == 8 : t[0] = Declaracion(t[1],t[3],t[6],None)
    elif len(t) == 5 : t[0] = Asignacion(t[1],t[3],None)
    elif len(t) == 9 : t[0] = Declaracion(t[2],t[4],t[7],t[1])#,t.lineno(2), find_column(inp, t.slice[2]),t[1])
    elif len(t) == 6 : t[0] = Asignacion(t[2],t[4],t[1])#t.lineno(2), find_column(inp, t.slice[2]),t[1])
    """elif len(t) == 4: t[0] = Asignacion(None,None,t[2],t.lineno(2), find_column(inp, t.slice[2]),t[1]) """

def p_asignacionArreglo(t):
    ''' asignacion : ID listaAccessoAr IGUAL expresiones PTCOMA 
    '''
    """ t[0] = AsignacionArreglo(t[4],t[2],t[1],1,1,None) """
def p_listaAccesoArray(t):
    '''listaAccessoAr : listaAccessoAr accesoArreglos '''
    if(t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]

def p_listaAccesoArray2(t):
    '''listaAccessoAr : accesoArreglos '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_accesoAcs(t):
    '''accesoArreglos : CORCHETEA exp CORCHETEC'''
    t[0] = t[2]

def p_listaParametros_G(t):
    'listaParametros : listaParametros COMA parametros'
    if(t[3] != ""):
        t[1].append(t[3])
    t[0] = t[1]
########################################################## SENTENCIAS DE TRANSFERENCIA ############################################
def p_traferencia(t):
    '''traferencia : RETURN expresiones PTCOMA
                    | BREAK PTCOMA
                    | CONTINUE  PTCOMA
    '''
    if t[1] == 'return': t[0] = Return(t[2])
    elif t[1] == 'break': t[0] =Break()
    elif t[1] == 'continue': t[0] =Continue()

############################################################ NATIVAS PARA ARREGLOS PTCOMA ###################################
def p_nativarArrayPtComa(t):
    '''nativaArayPtC : nativasArray PTCOMA'''
    t[0] = t[1]

######################################################### NATIVAS PARA ARREGLOS ###################################################33
def p_nativasarrays(t):
    '''nativasArray : PUSH NOT PARENTESISABIERTO exp COMA exp PARENTESISCERRADO 
                    | POP NOT PARENTESISABIERTO exp PARENTESISCERRADO 
                    | LENGTH PARENTESISABIERTO exp PARENTESISCERRADO 
    '''
    """ if t[1] == 'push': t[0] = NativasArray(tipoNativa.PUSH,t[4],t[6])
    elif t[1] == 'pop': t[0] = NativasArray(tipoNativa.POP,t[4],None)
    elif t[1] == 'length': t[0] = NativasArray(tipoNativa.LENGTH,t[3],None) """
####################################################### FUNCIONES #####################################################
def p_funcion(t):
    '''funcion : FUNCTION ID PARENTESISABIERTO listaParametros PARENTESISCERRADO DSPUNTOS DSPUNTOS tipos cuerpoFuncion END PTCOMA
                | FUNCTION ID PARENTESISABIERTO PARENTESISCERRADO DSPUNTOS DSPUNTOS tipos cuerpoFuncion END PTCOMA
    '''
    if len(t) == 12: t[0] = Function(t[2],t[4],t[9],t[8])#,t.lineno(1), find_column(inp, t.slice[1]))
    elif len(t) == 11: t[0] = Function(t[2],None,t[8],t[7])#,t.lineno(1), find_column(inp, t.slice[1]))

def p_listaParametros(t):
    '''listaParametros :  parametros
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_parametros(t):
    '''parametros : ID DSPUNTOS DSPUNTOS tipos
    '''
    if len(t) == 5: t[0] = (t[1],t[4])


################################################# LLAMADA DE FUNCIONES ###################################################
def p_llamadaFuncion(t):
    '''llamadaFunc : ID PARENTESISABIERTO listaValores PARENTESISCERRADO PTCOMA
                | ID PARENTESISABIERTO PARENTESISCERRADO PTCOMA
    '''
    if len(t) == 6: t[0] = LLamadaFuncion(t[1],t[3])
    elif len(t) == 5: t[0] = LLamadaFuncion(t[1],None)

def p_listaValores(t):
    '''listaValores : listaValores COMA expresiones'''
    if(t[3] != ""):
        t[1].append(t[3])
    t[0] = t[1]

def p_listaValores2(t):
    '''listaValores : expresiones'''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

################################################################# IFS ##########################################################
def p_IFS(t):
    ''' ifs : IF expresiones cuerpoFuncion elseifs ELSE cuerpoFuncion END PTCOMA
            | IF expresiones cuerpoFuncion ELSE cuerpoFuncion END PTCOMA
            | IF expresiones cuerpoFuncion elseifs END PTCOMA
            | IF expresiones cuerpoFuncion  END PTCOMA
    '''   
    if len(t) ==6 : t[0] = If(t[2],t[3])
    elif len(t) ==8 : t[0] = IfElse(t[2],t[3],t[5])
    elif len(t) == 7: t[0] = ElseIf(t[2],t[3],t[4])
    elif len(t) == 9: t[0] = ElseIfElse(t[2],t[3],t[4],t[6])
def p_ELSEIFS(t):
    '''elseifs : elseifs conelseif
    '''
    if(t[2] != ""):
        t[1].append(t[2])
    t[0] = t[1]

def p_ELSEIFS_3(t):
    '''elseifs : conelseif'''
    
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_ConElseIf(t):
    ''' conelseif : ELSEIF expresiones cuerpoFuncion'''
    t[0] = (t[2],t[3])


################################################################# WHILE ###########################################
def p_Instruccion_While(t):
    '''whiles : WHILE expresiones cuerpoFuncion END PTCOMA'''
    t[0] = While(t[2],t[3])
def p_tipo(t):
    '''tipos : INT
            | FLOAT
            | STRING
            | BOOL
            | CHAR
    '''
    if t[1] == 'Int64' : t[0] = tipoExpresion.INTEGER
    elif t[1] == 'Float64' : t[0] = tipoExpresion.FLOAT
    elif t[1]== 'Bool' : t[0] = tipoExpresion.BOOL
    elif t[1] == 'String' : t[0] = tipoExpresion.STRING
    elif t[1] == 'Char' : t[0] = tipoExpresion.CHAR 
    

def p_expresiones(t):
    ''' expresiones : exp
    '''
    t[0] = t[1]
######################################################### FUNCIONES NATIVAS ##############################################
def p_nativas(t):
    ''' nativas : UPPERCASE PARENTESISABIERTO exp PARENTESISCERRADO
                | LOWERCASE PARENTESISABIERTO exp PARENTESISCERRADO
                | PARSE PARENTESISABIERTO tipos COMA exp PARENTESISCERRADO
                | TRUNC PARENTESISABIERTO tipos COMA exp PARENTESISCERRADO
                | FLOAT_ PARENTESISABIERTO exp PARENTESISCERRADO
                | STRING_ PARENTESISABIERTO exp PARENTESISCERRADO
                | TYPEOF PARENTESISABIERTO exp PARENTESISCERRADO
    '''
    """ if t[1] == 'log10' : t[0] = Nativa(t[3],None,tipoNativa.LOG10)
    elif t[1] == 'log' : t[0] = Nativa(t[3],t[5],tipoNativa.LOG)
    elif t[1] == 'sin' : t[0] = Nativa(t[3],None,tipoNativa.SIN)
    elif t[1] == 'cos' : t[0] = Nativa(t[3],None,tipoNativa.COS)
    elif t[1] == 'tan' : t[0] = Nativa(t[3],None,tipoNativa.TAN)
    elif t[1] == 'sqrt' : t[0] = Nativa(t[3],None,tipoNativa.SQRT)
    elif t[1] == 'uppercase' : t[0] = Nativa(t[3],None,tipoNativa.UPPERCASE)
    elif t[1] == 'lowercase' : t[0] = Nativa(t[3],None,tipoNativa.LOWERCASE)
    elif t[1] == 'parse' : t[0] = Nativa(t[5],t[3],tipoNativa.PARSE)
    elif t[1] == 'trunc' : t[0] = Nativa(t[5],t[3],tipoNativa.TRUNC)
    elif t[1] == 'float' : t[0] = Nativa(t[3],None,tipoNativa.FLOAT)"""
    if t[1] == 'string' : t[0] = StringNative(t[3])
def p_expresion_operacion(t):
    ''' exp : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | exp POTENCIA exp
            | exp MODULO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
            | exp IGUALIGUAL exp
            | exp DIFERENTE exp
            | exp AND exp
            | exp OR exp
            | NOT exp  %prec UNOT
            | MENOS exp %prec UMINUS

    '''
    if t[2] == '+' : t[0] = Suma(t[1],t[3])
    elif t[2] == '-' : t[0] = Resta(t[1],t[3])
    elif t[2] == '*' : t[0] = Multiplicacion(t[1],t[3])
    elif t[2] == '/' : t[0] = Division(t[1],t[3])
    elif t[1] == '-' : t[0] = RestaU(t[2])
    elif t[2] == '==' : t[0] = IgualIgual(t[1],t[3])
    elif t[2] == '>' : t[0] = Mayor(t[1],t[3])
    elif t[2] == '<' : t[0] = Menor(t[1],t[3])
    elif t[2] == '>=' : t[0] = MayorIgual(t[1],t[3])
    elif t[2] == '<=' : t[0] = MenorIgual(t[1],t[3])
    elif t[2] == '!=' : t[0] = Diferente(t[1],t[3])
    elif t[2] == '%' : t[0] = Modulo(t[1],t[3])
    elif t[2] == '^' : t[0] = Potencia(t[1],t[3])
    elif t[2] == '&&' : t[0] = And(t[1],t[3])
    elif t[2] == '||' : t[0] = Or(t[1],t[3])
    elif t[1] == '!' : t[0] = Not(t[2])
    

def p_expresion_agrupacion(t):
    '''exp : PARENTESISABIERTO exp PARENTESISCERRADO'''
    t[0] = t[2]

def p_expresion_entero(t):
    '''exp : ENTERO'''
    t[0] = NumberVal(tipoExpresion.INTEGER,t[1]) 

def p_expresion_decimal(t):
    '''exp : DECIMAL'''   
    t[0] = NumberVal(tipoExpresion.FLOAT,t[1]) 

def p_exp_Nativas(t):
    '''exp : nativas'''
    t[0] = t[1]

def p_exp_NativasArray(t):
    '''exp : nativasArray'''
    t[0] = t[1]

def p_expresion_cadena(t):
    '''exp : CADENA'''
    t[0] = TextVal(tipoExpresion.STRING,t[1])

def p_expresion_caracter(t):
    '''exp : CARACTER'''
    t[0] = TextVal(tipoExpresion.CHAR,t[1])

def p_expresion_id(t):
    '''exp : ID'''
    t[0] = Identificador(t[1])

def p_expresion_acceso(t):
    '''exp : ID listaAccessoAr'''
    """ t[0] = AccesoArray(t[1],t[2]) """

def p_expresion_arreglo(t):
    '''exp : CORCHETEA listaValores CORCHETEC'''
    """ t[0] = Arreglo(t[2],tipoExpresion.ARREGLO) """

def p_expresion_func(t):
    '''exp : ID PARENTESISABIERTO listaValores PARENTESISCERRADO '''
    t[0] = LLamadaFuncion(t[1],t[3])
def p_expresion_func2(t):
    '''exp : ID PARENTESISABIERTO PARENTESISCERRADO '''
    t[0] = LLamadaFuncion(t[1],None)

def p_expresion_false(t):
    '''exp : FALSE'''
    t[0] = BoolVal(tipoExpresion.BOOL,0)
def p_expresion_true(t):
    '''exp : TRUE'''
    t[0] = BoolVal(tipoExpresion.BOOL,1)
def p_error(t):
    print("Error sintactico en '%s'" % t.value)
def getErrores():
    return errores
import ply.yacc as yacc

inp = ""

parser = yacc.yacc()
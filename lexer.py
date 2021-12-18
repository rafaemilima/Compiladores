'''
tokens:

identificadores

ID

delimitadores

DELI_INITIATE  
DELI_HALT


Palavras reservadas

RESE_CENTRAL
RESE_FUNCAO
RESE_RETORNA
RESE_INT
RESE_STR
RESE_FLOAT
RESE_CHAR
RESE_BOOL
RESE_ARRAY
BOOL_VERDADE
BOOL_FALSO
RESE_SE
RESE_SENAO
RESE_LOOP
RESE_ENQUANTO
RESE_NULO
RESE_PARE
RESE_LER
RESE_ESCREVER

Operadores

OPE_ADI +
OPE_SUB - 
OPE_MULTI *
OPE_DIVI /
OPE_REST %
OPE_EXPO ^
OPE_UNARYNEG -
OPE_IGUAL ==
OPE_DIF !=
OPE_MENORQ <
OPE_MAIORQ >
OPE_MENORI <=
OPE_MAIORI >=
OPE_NEGA !
OPE_CONJUN 'E'
OPE_DISJUN 'OU'
OPE_CONCAT @

CONSTANTES

CTE_INT
CTE_FLO
CTE_STR
CTE_CHR
CTR_BOOL


'''


cod = "Funcao Int Central () Initiate x = 12 Halt"



import re                                 # for performing regex expressions

tokens = []                               # for string tokens
source_code = cod.split() # turning source code into list of words

# Loop through each source code word
for char in source_code:
    
    # This will check if a token has datatype decleration

    delimiters = ['Initiate', 'Halt']
    reserved = ['Central', 'Funcao', 'Retorna', 'Int', 'Str', 'Float'
    ,'Char', 'Bool', 'Array', 'Verdadeiro', 'Falso', 'Se', 'SeNao',
     'Loop', 'Enquanto', 'Nulo', 'Pare', 'Ler', 'Escrever']

    operators =['+', '-', '*', '/', '%', '^', '-'  #aritmeticos
                '==','!=', '<', '>', '<=', '>=',    #relacionais
                '!','E', 'Ou'                      #logicos 
                ,'@']                               #concatenação



    if char in reserved:       
        tokens.append(['RESE', char])
    
    elif char in delimiters:
        tokens.append(['DELI', char])

    # This will look for an identifier which would be just a word
    elif re.match("[a-z]", char) or re.match("[A-Z]", char):
        tokens.append(['ID', char])
    
    # This will look for an operator
    elif char in operators:
        tokens.append(['OPE', char])
    
    # This will look for integer items and cast them as a number
    elif re.match(".[0-9]", char):
        if char[len(char) - 1] == ';': 
            tokens.append(["RESE_INT", char[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", char])

print(tokens) # Outputs the token array
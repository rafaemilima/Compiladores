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
'''




import re                                 # for performing regex expressions

tokens = []                               # for string tokens
source_code = 'int result = 100;'.split() # turning source code into list of words

# Loop through each source code word
for word in source_code:
    
    # This will check if a token has datatype decleration

    delimiters = ['Initiate', 'Halt']
    reserved = ['Central', 'Funcao', 'Retorna', 'Int', 'Str', 'Float'
    ,'Char', 'Bool', 'Array', 'Verdadeiro', 'Falso', 'Se', 'SeNao',
     'Loop', 'Enquanto', 'Nulo', 'Pare', 'Ler', 'Escrever']

    operators =['+', '-', '*', '/', '%', '^', '-'  #aritmeticos
                '==','!=', '<', '>', '<=', '>=',    #relacionais
                '!','E', 'Ou'                      #logicos 
                ,'@']                               #concatenação





    if word in reserved: 
        tokens.append(['RESERVED', word])
    
    # This will look for an identifier which would be just a word
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    
    # This will look for an operator
    elif word in '*-/+%=':
        tokens.append(['OPERATOR', word])
    
    # This will look for integer items and cast them as a number
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';': 
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else: 
            tokens.append(["INTEGER", word])

print(tokens) # Outputs the token array
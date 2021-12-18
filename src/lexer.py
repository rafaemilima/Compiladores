
cod = "Funcao Int Central () Initiate x = 12; Halt"

import re
from typing import Dict                                 # for performing regex expressions

tokens = []                               # for string tokens
source_code = cod.split() # turning source code into list of words


Dict_reserved = {'Central' : "RESE_CENTRAL",
            'Funcao'  : "RESE_FUNCAO",
            'Retorna' : "RESE_RETORNA",
            'Int' : "RESE_INT",
            'Str' : "RESE_STR",
            'Float':"RESE_FLOAT",
            'Char': "RESE_CHAR",
            'Bool' : "RESE_BOOL",
            "Array": "RESE_ARRAY",
            'Verdade': "RESE_VERDADE",
            'Falso': "RESE_FALSO",
            'Se': "RESE_SE",
            'SeNao': "RESE_SENAO",
            'Loop': "RESE_LOOP",
            "Enquanto": "RESE_ENQUANTO",
            "Nulo": "RESE_NULO",
            "Pare": "RESE_PARE",
            "Ler": "RESE_LER",
            "Escrever": "RESE_ESCREVER"}

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
        tokens.append([Dict_reserved[char], char])
    
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

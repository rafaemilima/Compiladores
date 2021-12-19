
class ReservedDict:
    reservedWords = {'Initiate': ["RESE_INITIATE", 1],
                     'Halt': ["RESE_HALT", 2],
                     'Central': ["RESE_CENTRAL", 3],
                     'Funcao': ["RESE_FUNCAO", 4],
                     'Retorna': ["RESE_RETORNA", 5],
                     'Int': ["RESE_INT", 6],
                     'Str': ["RESE_STR", 7],
                     'Float': ["RESE_FLOAT", 8],
                     'Char': ["RESE_CHAR", 9],
                     'Bool': ["RESE_BOOL", 10],
                     "Array": ["RESE_ARRAY", 11],
                     "Vazio": ["RESE_VAZIO", 12],
                     'Verdade': ["RESE_VERDADE", 13],
                     'Falso': ["RESE_FALSO", 14],
                     'Se': ["RESE_SE", 15],
                     'SeNao': ["RESE_SENAO", 16],
                     'Loop': ["RESE_LOOP", 17],
                     "Enquanto": ["RESE_ENQUANTO", 18],
                     "Nulo": ["RESE_NULO", 19],
                     "Pare": ["RESE_PARE", 20],
                     "Ler": ["RESE_LER", 21],
                     "Escrever": ["RESE_ESCREVER", 22],
                     "Escreverpl": ["RESE_ESCREVERPL", 23],
                     "E": ["OPE_CONJUN", 24],
                     "Ou": ["OPE_DISJUN", 25]}

    operators = {"+": ["OPE_ADI", 26],
                 "-": ["OPE_SUB", 27],
                 "*": ["OPE_MULTI", 28],
                 "/": ["OPE_DIV", 29],
                 "%": ["OPE_REST", 30],
                 "=": ["OPE_ATRI", 31],
                 "¬": ["OPE_UNARINEG", 32],
                 "OPE_RELA": ["OPE_RELA", 33],
                 "<": ["OPE_MENORQ", 34],
                 ">": ["OPE_MAIORQ", 35],
                 "OPE_MENORI": ["OPE_MENORI", 36],
                 "OPE_MAIORI": ["OPE_MAIORI", 37],
                 "!": ["OPE_NEGA", 38],
                 "@": ["OPE_CONCAT", 39]}

    identifier = {"ID": ["ID", 40],
                  "CNST_INT": ["CNST_INT", 41],
                  "CNST_FLOAT": ["CNST_FLOAT", 42],
                  "BOOL_VALUE": ["BOOL_VALUE", 43]}

    delimiters = {"CNST_CHAR": ["CNST_CHAR", 44],
                   "CNST_STR": ["CNST_STR", 45],
                   "DELI_INITIATE": ["DELI_INITIATE",46],
                   "DELI_HALT": ["DELI_HALT", 47],
                   '(': ["DELI_OPAREN", 48],
                   ')': ["DELI_CPAREN", 49],
                   ']': ["DELI_ENBRA", 50],
                   '[': ["DELI_OPBRA", 51],
                   ',': ["DELI_COMMA", 52],
                   ';': ["DELI_SECOL", 53]}

    errors = {"ERR_UNK": ["ERR_IND", 54],
              "ERR_IND": ["ERR_IND", 55],
              "ERR_NUMER": ["ERR_NUMER", 56],
              "ERR_PR": ["ERR_PR", 57],
              "ERR_CHR": ["ERR_CHR", 58]}

    etc = {"ETC_EOF": ["ETC_EOF",59],
           "ETC_COMMENT": ["ETC_COMMENT", 60]}

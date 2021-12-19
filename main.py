import sys
from lex import *

string = ""
token = Lexer(sys.argv[1])

while not token.isEOF():

    currTkn = token.getNextToken()

    print(currTkn.toString())

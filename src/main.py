import sys
from lex import *

string = ""
token = Lexer(sys.argv[1])

while not token.isEOF():

    currTkn = token.nextToken()

    print(currTkn.toString())

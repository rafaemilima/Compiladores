from dictPyr import *
from tkn import *
from validate import *


class State (ABC):
    def __init__(self, lexer):
        self.lexer = lexer

    @abstractmethod
    def processState(self, curr_char):
        pass


class StateZero(State):
    def processState(self, curr_char):
        if Blank(curr_char).validate():
            self.lexer.state = 0

        elif LowerCase(curr_char).validate():
            self.lexer.lexem += curr_char
            self.lexer.state = 1

        elif Digit(curr_char).validate():
            self.lexer.lexem += curr_char
            self.lexer.state = 3

        elif Operator(curr_char).validate():
            self.lexer.lexem += curr_char
            self.lexer.state = 7

        elif curr_char == '\'':
            self.lexer.lexem += curr_char
            self.lexer.state = 8

        elif UpperCase(curr_char).validate():
            self.lexer.lexem += curr_char
            self.lexer.state = 11

        elif curr_char == '#':
            self.lexer.lexem += curr_char
            self.lexer.state = 13

        elif curr_char in ['+', '-', '*', '/', '%', '¬', '@']:
            self.lexer.lexem += curr_char
            self.lexer.col += 1
            return Token(ReservedDict.operators[curr_char][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif curr_char in ['(', ')', '[', ']', ';', ',']:
            self.lexer.lexem += curr_char
            self.lexer.col += 1
            return Token(ReservedDict.delimiters[curr_char][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            Token(ReservedDict.errors['ERR_UNK'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateOne(State):
    def processState(self, curr_char):
        if Operator(curr_char).validate() or Blank(curr_char).validate() or not Alphanum(curr_char).validate():
            self.lexer.back()
            self.lexer.state = 2

        elif Digit(curr_char).validate() or LowerCase(curr_char).validate() or UpperCase(curr_char).validate():
            self.lexer.lexem += curr_char

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_IND'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateTwo(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['ID'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateThree(State):
    def processState(self, curr_char):
        if curr_char == '.':
            self.lexer.lexem += curr_char
            self.lexer.state = 4
            self.lexer.col = +1
        elif not Alphanum(curr_char).validate():
            self.lexer.back()
            self.lexer.state = 5
        elif Digit(curr_char).validate():
            self.lexer.lexem += curr_char
        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_NUMER'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateFour(State):
    def processState(self, curr_char):
        if Digit(curr_char).validate():
            self.lexer.lexem += curr_char

        elif Operator(curr_char).validate() or Blank(curr_char).validate() or not Alphanum(curr_char).validate():
            self.lexer.back()
            self.lexer.state = 6

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_NUMER'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateFive(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['CNST_INT'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateSix(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['CNST_FLOAT'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateSeven(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.back()
        curr_char = self.lexer.getNextChar()

        if curr_char == '>':
            curr_char = self.lexer.getNextChar()
            self.lexer.col += 1

            if curr_char == '=':
                self.lexer.lexem += curr_char
                return Token(ReservedDict.operators['OPE_MAIORI'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['>'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif curr_char == '<':

            curr_char = self.lexer.getNextChar()
            self.lexer.col += 1

            if curr_char == '=':
                self.lexer.lexem += curr_char
                return Token(ReservedDict.operators['OPE_MENORI'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['<'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif curr_char == '!' or curr_char == '=':
            curr_char = self.lexer.getNextChar()
            self.lexer.col += 1

            if curr_char == '=':
                self.lexer.lexem += curr_char
                return Token(ReservedDict.operators['OPE_RELA'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['!'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            Token(ReservedDict.errors['ERR_UNK'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateEight(State):
    def processState(self, curr_char):
        if chr(32) <= curr_char <= chr(126):
            self.lexer.lexem += curr_char
            curr_char = self.lexer.getNextChar()

            if curr_char == '\'':
                self.lexer.lexem += curr_char
                self.lexer.state = 9

            else:
                self.lexer.back()
                self.lexer.state = 10

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_CHR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateNine(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.delimiters['CNST_CHAR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateTen(State):
    def processState(self, curr_char):
        if chr(32) <= curr_char <= chr(126):
            self.lexer.lexem += curr_char

            if curr_char == '\'':
                self.lexer.col += 1
                return Token(ReservedDict.delimiters['CNST_STR'], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_CHR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateEleven(State):
    def processState(self, curr_char):
        if not (LowerCase(curr_char).validate()) or Blank(curr_char).validate():
            self.lexer.back()
            self.lexer.state = 12

        elif LowerCase(curr_char).validate():
            self.lexer.lexem += curr_char


class StateTwelve(State):
    def processState(self, curr_char):
        self.lexer.back()
        self.lexer.col += 1

        if ReservedDict.reservedWords[self.lexer.lexem] is not None:
            return Token(ReservedDict.reservedWords[self.lexer.lexem], self.lexer.lexem, self.lexer.row,
                         self.lexer.col)
        else:
            return Token(ReservedDict.errors["ERR_PR"], self.lexer.lexem, self. lexer.row, self.lexer.col)
            self.lexer.back()
            self.lexer.col += 1

            if WordDict.words[lexem] is not None:
                return Token(ReservedDict.reservedWords[self.lexer.lexem], self.lexer.lexem, self.lexer.row,
                             self.lexer.col)
            else:
                return Token(ReservedDict.errors["ERR_PR"], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateThirteen(State):
    def processState(self, curr_char):
        self.lexer.newLine()
        self.lexer.content = self.lexer.txtline
        self.lexer.lexem = ''
        self.lexer.state = 0

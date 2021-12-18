import traceback
from abc import ABC, abstractmethod
from tk import *
from wordDict import *

class Lexer:

    def __init__(self, file):
        try:
            self.txtline = " "
            self.pos = 1
            self.row = 1
            self.col = 1
            self.reader = open(file, 'rb')
            self.new_line()
            self.lexem = ''

            self.content = list(self.txtline)
            self.state = None

        except IOError as e:
            traceback.print_exc()


    @staticmethod
    def is_digit(string):
        return string.isdigit()

    @staticmethod
    def is_operator(string):

        return string in ['>', '<', '=', '!']

    @staticmethod
    def is_lower(string):
        return string.islower()

    @staticmethod
    def is_upper(string):
        return string.isupper()

    @staticmethod
    def is_blank(string):
        return string.isspace()

    @staticmethod
    def is_letter(string):
        return string.isalpha()

    @staticmethod
    def is_alphanum(string):
        return string.isalpha() or string.isdigit()

    def is_EOF(self):
        return self.pos == len(self.content)

    def next_char(self):
        self.pos += 1
        return self.content[self.pos - 1]

    def next_token(self):
        self.state = 0
        self.lexem = ""
        while True:

            if self.is_EOF():
                if self.new_line():
                    self.content = list(self.txtline)
                else:
                    return Token(ReservedDict.etc["ETC_EOF"], "EOF", self.row, self.col)

            currChar = self.next_char()
            curState = None
            check = None

            if self.state == 0:
                curState = StateZero(self)

            elif self.state == 1:
                curState = StateOne(self)

            elif self.state == 2:
                curState = StateTwo(self)

            elif self.state == 3:
                curState = StateThree(self)

            elif self.state == 4:
                curState = StateFour(self)

            elif self.state == 5:
                curState = StateFive(self)

            elif self.state == 6:
                curState = StateSix(self)

            elif self.state == 7:
                curState = StateSeven(self)

            elif self.state == 8:
                curState = StateEight(self)

            elif self.state == 9:
                curState = StateNine(self)

            elif self.state == 10:
                curState = StateTen(self)

            elif self.state == 11:
                curState = StateEleven(self)

            elif self.state == 12:
                curState = StateTwelve(self)

            elif self.state == 13:
                curState = StateThirteen(self)

            check = curState.processState(currChar)
            if check:
                return check

    def back(self):
        self.pos -= 1

    def new_line(self):

        tmp = ''

        try:
            tmp = self.reader.readline().decode("utf-8")

        except IOError as e:
            traceback.print_exc()

        if tmp != '':
            self.txtline = tmp

            print(f"{self.row} {self.txtline}")

            self.txtline += " "
            self.row += 1
            self.pos = 0
            self.col = 0

            return True

        return False


class State (ABC):
    def __init__(self, lexer):
        self.lexer = lexer

    @abstractmethod
    def processState(self, currchar):
        pass


class StateZero(State):
    def processState(self, currChar):
        if self.lexer.is_blank(currChar):
            self.lexer.state = 0

        elif self.lexer.is_lower(currChar):
            self.lexer.lexem += currChar
            self.lexer.state = 1

        elif self.lexer.is_digit(currChar):
            self.lexer.lexem += currChar
            self.state = 3

        elif self.lexer.is_operator(currChar):
            self.lexer.lexem += currChar
            self.lexer.state = 7

        elif currChar == '\'':
            self.lexer.lexem += currChar
            self.lexer.state = 8

        elif self.lexer.is_upper(currChar):
            self.lexer.lexem += currChar
            self.lexer.state = 11

        elif currChar == '#':
            self.lexer.lexem += currChar
            self.lexer.state = 13

        elif currChar in ['+', '-', '*', '/', '%', '¬', '@']:
            self.lexer.lexem += currChar
            self.lexer.col += 1
            return Token(ReservedDict.operators[currChar][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif currChar in ['(', ')', '[', ']', ';', ',']:
            self.lexer.lexem += currChar
            self.lexer.col += 1
            return Token(ReservedDict.delimiters[currChar][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            Token(ReservedDict.errors['ERR_UNK'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateOne(State):
    def processState(self, currChar):
        if self.lexer.is_operator(currChar) or self.lexer.is_blank(currChar) or not self.lexer.is_alphanum(currChar):
            self.lexer.back()
            self.state = 2

        elif self.lexer.is_digit(currChar) or self.lexer.is_lower(currChar) or self.lexer.is_upper(currChar):
            self.lexer.lexem += currChar

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_IND'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateTwo(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['ID'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateThree(State):
    def processState(self, currChar):
        if currChar == '.':
            self.lexer.lexem += currChar
            self.lexer.state = 4
            self.lexer.col = +1
        elif not self.lexer.is_alphanum(currChar):
            self.lexer.back()
            self.lexer.state = 5
        elif self.lexer.is_digit(currChar):
            self.lexer.lexem += currChar
        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_NUMER'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateFour(State):
    def processState(self, currChar):
        if self.lexer.is_digit(currChar):
            self.lexer.lexem += currChar

        elif self.lexer.is_operator(currChar) or self.lexer.is_blank(currChar) or not self.lexer.is_alphanum(currChar):
            self.lexer.back()
            self.lexer.state = 6

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_NUMER'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateFive(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['CNST_INT'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateSix(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.identifier['CNST_FLOAT'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateSeven(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.back()
        currChar = self.lexer.next_char()

        if currChar == '>':
            currChar = self.lexer.next_char()
            self.lexer.col += 1

            if currChar == '=':
                self.lexer.lexem += currChar
                return Token(ReservedDict.operators['OPE_MAIORI'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['>'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif currChar == '<':

            currChar = self.lexer.next_char()
            self.lexer.col += 1

            if currChar == '=':
                self.lexer.lexem += currChar
                return Token(ReservedDict.operators['OPE_MENORI'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['<'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        elif currChar == '!' or currChar == '=':
            currChar = self.lexer.next_char()
            self.lexer.col += 1

            if currChar == '=':
                self.lexer.lexem += currChar
                return Token(ReservedDict.operators['OPE_RELA'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                self.lexer.back()
                return Token(ReservedDict.operators['!'][1], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            Token(ReservedDict.errors['ERR_UNK'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateEight(State):
    def processState(self, currChar):
        if chr(32) <= currChar <= chr(126):
            self.lexer.lexem += currChar
            currChar = self.lexer.next_char()

            if currChar == '\'':
                self.lexer.lexem += currChar
                self.state = 9

            else:
                self.lexer.back()
                self.lexer.state = 10

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_CHR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateNine(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.col += 1
        return Token(ReservedDict.delimiters['CNST_CHAR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateTen(State):
    def processState(self, currChar):
        if chr(32) <= currChar <= chr(126):
            self.lexer.lexem += currChar

            if currChar == '\'':
                self.lexer.col += 1
                return Token(ReservedDict.delimiters['CNST_STR'], self.lexer.lexem, self.lexer.row, self.lexer.col)

        else:
            self.lexer.col += 1
            Token(ReservedDict.errors['ERR_CHR'], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateEleven(State):
    def processState(self, currChar):
        if not (self.lexer.is_lower(currChar)) or self.lexer.is_blank(currChar):
            self.lexer.back()
            self.lexer.state = 12

        elif self.lexer.is_lower(currChar):
            self.lexer.lexem += currChar


class StateTwelve(State):
    def processState(self, currChar):
        self.lexer.back()
        self.lexer.col += 1

        if ReservedDict.reservedWords[self.lexer.lexem] is not None:
            return Token(ReservedDict.reservedWords[self.lexer.lexem], self.lexer.lexem, self.lexer.row, self.lexer.col)
        else:
            return Token(ReservedDict.errors["ERR_PR"], self.lexer.lexem, self. lexer.row, self.lexer.col)
            self.lexer.back()
            self.lexer.col += 1

            if WordDict.words[lexem] is not None:
                return Token(ReservedDict.reservedWords[self.lexer.lexem], self.lexer.lexem, self.lexer.row, self.lexer.col)
            else:
                return Token(ReservedDict.errors["ERR_PR"], self.lexer.lexem, self.lexer.row, self.lexer.col)


class StateThirteen(State):
    def processState(self, currChar):
        self.lexer.new_line()
        self.lexer.content = self.lexer.txtline
        self.lexer.lexem = ''
        self.lexer.state = 0

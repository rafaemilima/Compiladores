from abc import ABC, abstractmethod


class Validation(ABC):
    def __init__(self, string):
        self.string = string

    @abstractmethod
    def validate(self):
        pass


class UpperCase(Validation):

    def validate(self):
        return self.string.isupper()


class LowerCase(Validation):
    def validate(self):
        return self.string.islower()


class Digit(Validation):
    def validate(self):
        return self.string.isdigit()


class Operator(Validation):
    def validate(self):
        return self.string in ['>', '<', '=', '!']


class Blank(Validation):
    def validate(self):
        return self.string.isspace()


class Letter(Validation):
    def validate(self):
        return self.string.isalpha()


class Alphanum(Validation):
    def validate(self):
        return self.string.isalpha() or self.string.isdigit()

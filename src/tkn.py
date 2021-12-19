
class Token():
    def __init__(self, category, lexem, row, col):
        self.category = category
        self.lexem = lexem
        self.row = row
        self.col = col

    def toString(self):
        return f"              [{self.row - 1},{self.col}] ({self.category[1]}, {self.category[0]}) {{{self.lexem}}}"

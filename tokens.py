class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)

class Operator(Token):
    def __init__(self,value):
        super().__init__("OPERATOR",value)

class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", value)
        
class Keyword(Token):
    def __init__(self, value):
        super().__init__("KEYWORD", value)
        
class Variable(Token):
    def __init__(self, value):
        super().__init__("VARIABLE", value)

# class String(Token):
#     pass
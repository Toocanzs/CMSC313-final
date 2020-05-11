import sys
from enum import Enum
import math

class TokenType(Enum):
    COMMAND = 1
    VALUE = 2


class Token:
    def __init__(self, tokenType, nameCharacters):
        self.tokenType = tokenType
        self.nameCharacters = nameCharacters

    def getString(self):
        return "".join(self.nameCharacters)


code = """
PUSH 2
PUSH 7
ADD
PRINT

PUSH 9
PUSH 9
MUL
PRINT

PUSH 10
PUSH 100
DIV
PRINT


PUSH 6
PUSH 9
SUB
PRINT

PUSH 8
PUSH 14
MOD
PRINT

PUSH 8
PUSH 2
EXP
PRINT

PUSH 4
FACT
PRINT

PUSH 3
FACT
PUSH 5
MUL
PUSH 3
ADD
PRINT
"""

print("Input code:")
print("-"*10)
print(code)
print("-"*10)

# tokenize
offset = 0
tokens = []
currentToken = None
while offset < len(code):
    char = code[offset]
    if char == ' ' or char == '\n' or char == '\r':
        if currentToken is not None:
            tokens.append(currentToken)
            currentToken = None
    elif char.isalpha() and char.isupper():
        if currentToken is None:
            currentToken = Token(TokenType.COMMAND, [])
        currentToken.nameCharacters.append(code[offset])
    elif char.isnumeric:
        if currentToken is None:
            currentToken = Token(TokenType.VALUE, [])
        currentToken.nameCharacters.append(code[offset])

    offset += 1
if(currentToken != None):#if the code doesn't end with whitespace or newline we need to still handle the last token
    tokens.append(currentToken)
    currentToken = None

stack = []

for i in range(len(tokens)):
    token = tokens[i]
    if token.tokenType == TokenType.COMMAND:
        if token.getString() == "PUSH":
            value = tokens[i + 1]
            stack.append(int(value.getString()))  # convert to int
            i += 1  # we visited the push token and the value token, so increment again

        elif token.getString() == "ADD":
            # grab two values off the stack, add them, push the result back on the stack
            stack.append(stack.pop() + stack.pop())
            
        elif token.getString() == "SUB":
            stack.append(stack.pop() - stack.pop())

        elif token.getString() == "MUL":
            stack.append(stack.pop() * stack.pop())

        elif token.getString() == "DIV":
            stack.append(stack.pop() // stack.pop())

        elif token.getString() == "MOD":
            stack.append(stack.pop() % stack.pop())

        elif token.getString() == "EXP":
            stack.append(int(math.pow(stack.pop(), stack.pop())))
            
        elif(token.getString() == "PRINT"):
            print(stack.pop())
            
        elif token.getString() == "FACT":
            stack.append(int(math.factorial(stack.pop())))

    i += 1  # go to the next token

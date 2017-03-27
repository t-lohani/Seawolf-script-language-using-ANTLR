# Tarun Lohani - 110921666

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SeawolfExprLexer import SeawolfExprLexer
from SeawolfExprParser import SeawolfExprParser
from antlr4.error.ErrorListener import ErrorListener
from MyVisitor import MyVisitor

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Oh no!!")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SeawolfExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfExprParser(token_stream)
    parser._listeners = [ MyErrorListener() ]
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
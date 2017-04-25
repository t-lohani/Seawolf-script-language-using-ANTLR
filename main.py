# Tarun Lohani - 110921666

import sys

from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error.ErrorListener import ErrorListener

from MyVisitor import MyVisitor
from SeawolfExprLexer import SeawolfExprLexer
from SeawolfExprParser import SeawolfExprParser


class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Synatax Error")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        # raise Exception("Report Ambiguity")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        # raise Exception("Report Attempting Full Context")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        # raise Exception("Report Context Sensitivity")
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SeawolfExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfExprParser(token_stream)
    errListener = MyErrorListener()

    parser.removeErrorListeners()
    lexer.removeErrorListeners()

    parser.addErrorListener(errListener)
    lexer.addErrorListener(errListener)

    try:
        tree = parser.prog()
        visitor = MyVisitor()
        try:
            visitor.visit(tree)
        except:
            print("SEMANTIC ERROR")
    except:
        print("SYNTAX ERROR")
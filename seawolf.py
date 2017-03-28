# Tarun Lohani - 110921666

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SeawolfExprLexer import SeawolfExprLexer
from SeawolfExprParser import SeawolfExprParser
from antlr4.error.ErrorListener import ErrorListener
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SeawolfExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfExprParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
# Generated from C:/Users/Tarun/PycharmProjects/POPL\SeawolfExpr.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SeawolfExprParser import SeawolfExprParser
else:
    from SeawolfExprParser import SeawolfExprParser

# This class defines a complete generic visitor for a parse tree produced by SeawolfExprParser.

class SeawolfExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SeawolfExprParser#prog.
    def visitProg(self, ctx:SeawolfExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#PrintExpr.
    def visitPrintExpr(self, ctx:SeawolfExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Blank.
    def visitBlank(self, ctx:SeawolfExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#BinaryNot.
    def visitBinaryNot(self, ctx:SeawolfExprParser.BinaryNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#FloorDivision.
    def visitFloorDivision(self, ctx:SeawolfExprParser.FloorDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Exponent.
    def visitExponent(self, ctx:SeawolfExprParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#BinaryAnd.
    def visitBinaryAnd(self, ctx:SeawolfExprParser.BinaryAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#MulDiv.
    def visitMulDiv(self, ctx:SeawolfExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#AddSub.
    def visitAddSub(self, ctx:SeawolfExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Parens.
    def visitParens(self, ctx:SeawolfExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Logical.
    def visitLogical(self, ctx:SeawolfExprParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#String.
    def visitString(self, ctx:SeawolfExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Int.
    def visitInt(self, ctx:SeawolfExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Modulus.
    def visitModulus(self, ctx:SeawolfExprParser.ModulusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#Real.
    def visitReal(self, ctx:SeawolfExprParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfExprParser#BinaryOr.
    def visitBinaryOr(self, ctx:SeawolfExprParser.BinaryOrContext):
        return self.visitChildren(ctx)



del SeawolfExprParser
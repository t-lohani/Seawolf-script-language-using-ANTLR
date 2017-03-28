from SeawolfExprVisitor import SeawolfExprVisitor
from SeawolfExprParser import SeawolfExprParser


class MyVisitor(SeawolfExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return int((ctx.INT().getText()))

    def visitNegNum(self, ctx):
        val = self.visit(ctx.expr())
        return val*-1

    def visitString(self, ctx):
        str = ctx.ID().getText()
        return str[1:-1]

    def visitReal(self, ctx):
        return float(ctx.REAL().getText())

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfExprParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfExprParser.ADD:
            return left + right
        return left - right

    def visitModulus(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left % right

    def visitExponent(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitFloorDivision(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left // right

    def visitLogical(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfExprParser.LESS:
            if left < right:
                return 1
            else:
                return 0
        elif ctx.op.type == SeawolfExprParser.LESSEQ:
            if left <= right:
                return 1
            else:
                return 0
        elif ctx.op.type == SeawolfExprParser.GRT:
            if left > right:
                return 1
            else:
                return 0
        elif ctx.op.type == SeawolfExprParser.GRTEQ:
            if left >= right:
                return 1
            else:
                return 0
        elif ctx.op.type == SeawolfExprParser.EQUAL:
            if left == right:
                return 1
            else:
                return 0
        elif ctx.op.type == SeawolfExprParser.NOTEQ:
            if left != right:
                return 1
            else:
                return 0

    def visitBinaryNot(self, ctx):
        val = self.visit(ctx.expr())
        if val == 0:
            return 1
        else:
            return 0

    def visitBinaryAnd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == 0 or right == 0:
            return 0
        else:
            return 1

    def visitBinaryOr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == 0 and right == 0:
            return 0
        else:
            return 1

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
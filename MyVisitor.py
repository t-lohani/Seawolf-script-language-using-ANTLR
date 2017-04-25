import sys

from SeawolfExprVisitor import SeawolfExprVisitor
from SeawolfExprParser import SeawolfExprParser


class MyVisitor(SeawolfExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssignStat(self, ctx):
        name = ctx.VAR().getText()
        expr_list = ctx.expr()

        if len(expr_list) == 1:
            self.memory[name] = self.visit(ctx.expr(0))
        else:
            index = []
            for expr in expr_list[:-1]:
                index.append(self.visit(expr))
            ret_val = self.update_ary(self.memory[name], index, self.visit(expr_list[-1]))
            self.memory[name] = ret_val

    def visitIfElseStat(self, ctx):
        val = self.visit(ctx.expr())
        block_list = ctx.block()
        if len(block_list) == 1:
            if val > 0:
                self.visit(ctx.block(0))
        else:
            if val > 0:
                self.visit(ctx.block(0))
            else:
                self.visit(ctx.block(1))

    def visitWhileStat(self, ctx):
        while (self.visit(ctx.expr()) > 0):
            self.visit(ctx.block())

    def update_ary(self, input, indices, val_to_update):
        if indices == []:
            return val_to_update
        input[indices[0]] = self.update_ary(input[indices[0]], indices[1:], val_to_update)
        return input

    def visitPrintStat(self, ctx):
        sys.stdout.write(str(self.visit(ctx.expr())))
        # print(self.visit(ctx.expr()))

    def visitVar(self, ctx):
        name = ctx.VAR().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitInt(self, ctx):
        return int((ctx.INT().getText()))

    def visitNegNum(self, ctx):
        val = self.visit(ctx.expr())
        return val*-1

    def visitString(self, ctx):
        str = ctx.STRING().getText()
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

    def visitList(self, ctx):
        ret_list = []
        list_start = ctx.list_expr()
        ret_list.append(self.visit(list_start.expr()))
        tail = list_start.list_expr()
        while not tail == None:
            ret_list.append(self.visit(tail.expr()))
            tail = tail.list_expr()
        return ret_list

    def visitIndexList(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left[right]

    def visitSearch(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left in right

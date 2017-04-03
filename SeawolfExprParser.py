# Generated from C:/Users/Tarun/PycharmProjects/POPL\SeawolfExpr.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\35")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4H\n\4\f\4\16\4K\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5S\n\5\3\5\2\3\6\6\2\4\6\b\2\5\3\2\b\t")
        buf.write("\3\2\n\13\3\2\17\24d\2\13\3\2\2\2\4\23\3\2\2\2\6%\3\2")
        buf.write("\2\2\bR\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\20\5\6\4\2\20")
        buf.write("\21\7\34\2\2\21\24\3\2\2\2\22\24\7\34\2\2\23\17\3\2\2")
        buf.write("\2\23\22\3\2\2\2\24\5\3\2\2\2\25\26\b\4\1\2\26\27\7\13")
        buf.write("\2\2\27&\5\6\4\23\30\31\7\3\2\2\31\32\5\6\4\2\32\33\7")
        buf.write("\4\2\2\33&\3\2\2\2\34\35\7\25\2\2\35&\5\6\4\13\36&\7\31")
        buf.write("\2\2\37&\7\32\2\2 &\7\33\2\2!\"\7\5\2\2\"#\5\b\5\2#$\7")
        buf.write("\6\2\2$&\3\2\2\2%\25\3\2\2\2%\30\3\2\2\2%\34\3\2\2\2%")
        buf.write("\36\3\2\2\2%\37\3\2\2\2% \3\2\2\2%!\3\2\2\2&I\3\2\2\2")
        buf.write("\'(\f\21\2\2()\t\2\2\2)H\5\6\4\22*+\f\20\2\2+,\7\f\2\2")
        buf.write(",H\5\6\4\21-.\f\17\2\2./\7\r\2\2/H\5\6\4\17\60\61\f\16")
        buf.write("\2\2\61\62\7\16\2\2\62H\5\6\4\17\63\64\f\r\2\2\64\65\t")
        buf.write("\3\2\2\65H\5\6\4\16\66\67\f\f\2\2\678\t\4\2\28H\5\6\4")
        buf.write("\r9:\f\n\2\2:;\7\26\2\2;H\5\6\4\13<=\f\t\2\2=>\7\27\2")
        buf.write("\2>H\5\6\4\n?@\f\b\2\2@A\7\30\2\2AH\5\6\4\tBC\f\3\2\2")
        buf.write("CD\7\5\2\2DE\5\6\4\2EF\7\6\2\2FH\3\2\2\2G\'\3\2\2\2G*")
        buf.write("\3\2\2\2G-\3\2\2\2G\60\3\2\2\2G\63\3\2\2\2G\66\3\2\2\2")
        buf.write("G9\3\2\2\2G<\3\2\2\2G?\3\2\2\2GB\3\2\2\2HK\3\2\2\2IG\3")
        buf.write("\2\2\2IJ\3\2\2\2J\7\3\2\2\2KI\3\2\2\2LM\5\6\4\2MN\7\7")
        buf.write("\2\2NO\5\b\5\2OS\3\2\2\2PS\5\6\4\2QS\3\2\2\2RL\3\2\2\2")
        buf.write("RP\3\2\2\2RQ\3\2\2\2S\t\3\2\2\2\b\r\23%GIR")
        return buf.getvalue()


class SeawolfExprParser ( Parser ):

    grammarFileName = "SeawolfExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "','", "'*'", 
                     "'/'", "'+'", "'-'", "'%'", "'**'", "'//'", "'<'", 
                     "'<='", "'>'", "'>='", "'=='", "'<>'", "'not'", "'and'", 
                     "'or'", "'in'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MUL", "DIV", "ADD", "SUB", 
                      "MOD", "EXP", "FLRDIV", "LESS", "LESSEQ", "GRT", "GRTEQ", 
                      "EQUAL", "NOTEQ", "NOT", "AND", "OR", "IN", "INT", 
                      "REAL", "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_list_expr = 3

    ruleNames =  [ "prog", "stat", "expr", "list_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    MUL=6
    DIV=7
    ADD=8
    SUB=9
    MOD=10
    EXP=11
    FLRDIV=12
    LESS=13
    LESSEQ=14
    GRT=15
    GRTEQ=16
    EQUAL=17
    NOTEQ=18
    NOT=19
    AND=20
    OR=21
    IN=22
    INT=23
    REAL=24
    ID=25
    NEWLINE=26
    WS=27

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.StatContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.StatContext,i)


        def getRuleIndex(self):
            return SeawolfExprParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SeawolfExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SeawolfExprParser.T__0) | (1 << SeawolfExprParser.T__2) | (1 << SeawolfExprParser.SUB) | (1 << SeawolfExprParser.NOT) | (1 << SeawolfExprParser.INT) | (1 << SeawolfExprParser.REAL) | (1 << SeawolfExprParser.ID) | (1 << SeawolfExprParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SeawolfExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(SeawolfExprParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(SeawolfExprParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = SeawolfExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SeawolfExprParser.T__0, SeawolfExprParser.T__2, SeawolfExprParser.SUB, SeawolfExprParser.NOT, SeawolfExprParser.INT, SeawolfExprParser.REAL, SeawolfExprParser.ID]:
                localctx = SeawolfExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(SeawolfExprParser.NEWLINE)
                pass
            elif token in [SeawolfExprParser.NEWLINE]:
                localctx = SeawolfExprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(SeawolfExprParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SeawolfExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.ExprContext,0)

        def NOT(self):
            return self.getToken(SeawolfExprParser.NOT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryNot" ):
                return visitor.visitBinaryNot(self)
            else:
                return visitor.visitChildren(self)


    class FloorDivisionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def FLRDIV(self):
            return self.getToken(SeawolfExprParser.FLRDIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloorDivision" ):
                return visitor.visitFloorDivision(self)
            else:
                return visitor.visitChildren(self)


    class ExponentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def EXP(self):
            return self.getToken(SeawolfExprParser.EXP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)


    class BinaryAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def AND(self):
            return self.getToken(SeawolfExprParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryAnd" ):
                return visitor.visitBinaryAnd(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(SeawolfExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(SeawolfExprParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def ADD(self):
            return self.getToken(SeawolfExprParser.ADD, 0)
        def SUB(self):
            return self.getToken(SeawolfExprParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class LogicalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def LESS(self):
            return self.getToken(SeawolfExprParser.LESS, 0)
        def LESSEQ(self):
            return self.getToken(SeawolfExprParser.LESSEQ, 0)
        def GRT(self):
            return self.getToken(SeawolfExprParser.GRT, 0)
        def GRTEQ(self):
            return self.getToken(SeawolfExprParser.GRTEQ, 0)
        def EQUAL(self):
            return self.getToken(SeawolfExprParser.EQUAL, 0)
        def NOTEQ(self):
            return self.getToken(SeawolfExprParser.NOTEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SeawolfExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SeawolfExprParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class NegNumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.ExprContext,0)

        def SUB(self):
            return self.getToken(SeawolfExprParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNum" ):
                return visitor.visitNegNum(self)
            else:
                return visitor.visitChildren(self)


    class ModulusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def MOD(self):
            return self.getToken(SeawolfExprParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulus" ):
                return visitor.visitModulus(self)
            else:
                return visitor.visitChildren(self)


    class SearchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def IN(self):
            return self.getToken(SeawolfExprParser.IN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearch" ):
                return visitor.visitSearch(self)
            else:
                return visitor.visitChildren(self)


    class RealContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(SeawolfExprParser.REAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)

        def OR(self):
            return self.getToken(SeawolfExprParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOr" ):
                return visitor.visitBinaryOr(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.List_exprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class IndexListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SeawolfExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SeawolfExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(SeawolfExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexList" ):
                return visitor.visitIndexList(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SeawolfExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SeawolfExprParser.SUB]:
                localctx = SeawolfExprParser.NegNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                localctx.op = self.match(SeawolfExprParser.SUB)
                self.state = 21
                self.expr(17)
                pass
            elif token in [SeawolfExprParser.T__0]:
                localctx = SeawolfExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(SeawolfExprParser.T__0)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(SeawolfExprParser.T__1)
                pass
            elif token in [SeawolfExprParser.NOT]:
                localctx = SeawolfExprParser.BinaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                localctx.op = self.match(SeawolfExprParser.NOT)
                self.state = 27
                self.expr(9)
                pass
            elif token in [SeawolfExprParser.INT]:
                localctx = SeawolfExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(SeawolfExprParser.INT)
                pass
            elif token in [SeawolfExprParser.REAL]:
                localctx = SeawolfExprParser.RealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(SeawolfExprParser.REAL)
                pass
            elif token in [SeawolfExprParser.ID]:
                localctx = SeawolfExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(SeawolfExprParser.ID)
                pass
            elif token in [SeawolfExprParser.T__2]:
                localctx = SeawolfExprParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(SeawolfExprParser.T__2)
                self.state = 32
                self.list_expr()
                self.state = 33
                self.match(SeawolfExprParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SeawolfExprParser.MulDivContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SeawolfExprParser.MUL or _la==SeawolfExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = SeawolfExprParser.ModulusContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 41
                        localctx.op = self.match(SeawolfExprParser.MOD)
                        self.state = 42
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = SeawolfExprParser.ExponentContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 44
                        localctx.op = self.match(SeawolfExprParser.EXP)
                        self.state = 45
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = SeawolfExprParser.FloorDivisionContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 47
                        localctx.op = self.match(SeawolfExprParser.FLRDIV)
                        self.state = 48
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = SeawolfExprParser.AddSubContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SeawolfExprParser.ADD or _la==SeawolfExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = SeawolfExprParser.LogicalContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SeawolfExprParser.LESS) | (1 << SeawolfExprParser.LESSEQ) | (1 << SeawolfExprParser.GRT) | (1 << SeawolfExprParser.GRTEQ) | (1 << SeawolfExprParser.EQUAL) | (1 << SeawolfExprParser.NOTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = SeawolfExprParser.BinaryAndContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        localctx.op = self.match(SeawolfExprParser.AND)
                        self.state = 57
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = SeawolfExprParser.BinaryOrContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        localctx.op = self.match(SeawolfExprParser.OR)
                        self.state = 60
                        self.expr(8)
                        pass

                    elif la_ == 9:
                        localctx = SeawolfExprParser.SearchContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        localctx.op = self.match(SeawolfExprParser.IN)
                        self.state = 63
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = SeawolfExprParser.IndexListContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 65
                        self.match(SeawolfExprParser.T__2)
                        self.state = 66
                        self.expr(0)
                        self.state = 67
                        self.match(SeawolfExprParser.T__3)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class List_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.ExprContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(SeawolfExprParser.List_exprContext,0)


        def getRuleIndex(self):
            return SeawolfExprParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = SeawolfExprParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_expr)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(SeawolfExprParser.T__4)
                self.state = 76
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         





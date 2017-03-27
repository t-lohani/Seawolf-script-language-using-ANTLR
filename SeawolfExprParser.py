# Generated from C:/Users/Tarun/PycharmProjects/POPL\SeawolfExpr.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\31")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\5\3\22\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4\36\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\2\3\6\5\2\4\6")
        buf.write("\2\5\3\2\5\6\3\2\7\b\3\2\f\21G\2\t\3\2\2\2\4\21\3\2\2")
        buf.write("\2\6\35\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13")
        buf.write("\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17")
        buf.write("\7\30\2\2\17\22\3\2\2\2\20\22\7\30\2\2\21\r\3\2\2\2\21")
        buf.write("\20\3\2\2\2\22\5\3\2\2\2\23\24\b\4\1\2\24\25\7\3\2\2\25")
        buf.write("\26\5\6\4\2\26\27\7\4\2\2\27\36\3\2\2\2\30\31\7\22\2\2")
        buf.write("\31\36\5\6\4\b\32\36\7\25\2\2\33\36\7\26\2\2\34\36\7\27")
        buf.write("\2\2\35\23\3\2\2\2\35\30\3\2\2\2\35\32\3\2\2\2\35\33\3")
        buf.write("\2\2\2\35\34\3\2\2\2\369\3\2\2\2\37 \f\16\2\2 !\t\2\2")
        buf.write("\2!8\5\6\4\17\"#\f\r\2\2#$\7\t\2\2$8\5\6\4\16%&\f\f\2")
        buf.write("\2&\'\7\n\2\2\'8\5\6\4\r()\f\13\2\2)*\7\13\2\2*8\5\6\4")
        buf.write("\f+,\f\n\2\2,-\t\3\2\2-8\5\6\4\13./\f\t\2\2/\60\t\4\2")
        buf.write("\2\608\5\6\4\n\61\62\f\7\2\2\62\63\7\23\2\2\638\5\6\4")
        buf.write("\b\64\65\f\6\2\2\65\66\7\24\2\2\668\5\6\4\7\67\37\3\2")
        buf.write("\2\2\67\"\3\2\2\2\67%\3\2\2\2\67(\3\2\2\2\67+\3\2\2\2")
        buf.write("\67.\3\2\2\2\67\61\3\2\2\2\67\64\3\2\2\28;\3\2\2\29\67")
        buf.write("\3\2\2\29:\3\2\2\2:\7\3\2\2\2;9\3\2\2\2\7\13\21\35\67")
        buf.write("9")
        return buf.getvalue()


class SeawolfExprParser ( Parser ):

    grammarFileName = "SeawolfExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'**'", "'//'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'<>'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "MOD", "EXP", "FLRDIV", "LESS", "LESSEQ", 
                      "GRT", "GRTEQ", "EQUAL", "NOTEQ", "NOT", "AND", "OR", 
                      "INT", "REAL", "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MUL=3
    DIV=4
    ADD=5
    SUB=6
    MOD=7
    EXP=8
    FLRDIV=9
    LESS=10
    LESSEQ=11
    GRT=12
    GRTEQ=13
    EQUAL=14
    NOTEQ=15
    NOT=16
    AND=17
    OR=18
    INT=19
    REAL=20
    ID=21
    NEWLINE=22
    WS=23

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SeawolfExprParser.T__0) | (1 << SeawolfExprParser.NOT) | (1 << SeawolfExprParser.INT) | (1 << SeawolfExprParser.REAL) | (1 << SeawolfExprParser.ID) | (1 << SeawolfExprParser.NEWLINE))) != 0)):
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
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SeawolfExprParser.T__0, SeawolfExprParser.NOT, SeawolfExprParser.INT, SeawolfExprParser.REAL, SeawolfExprParser.ID]:
                localctx = SeawolfExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(SeawolfExprParser.NEWLINE)
                pass
            elif token in [SeawolfExprParser.NEWLINE]:
                localctx = SeawolfExprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SeawolfExprParser.T__0]:
                localctx = SeawolfExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 18
                self.match(SeawolfExprParser.T__0)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(SeawolfExprParser.T__1)
                pass
            elif token in [SeawolfExprParser.NOT]:
                localctx = SeawolfExprParser.BinaryNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                localctx.op = self.match(SeawolfExprParser.NOT)
                self.state = 23
                self.expr(6)
                pass
            elif token in [SeawolfExprParser.INT]:
                localctx = SeawolfExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(SeawolfExprParser.INT)
                pass
            elif token in [SeawolfExprParser.REAL]:
                localctx = SeawolfExprParser.RealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(SeawolfExprParser.REAL)
                pass
            elif token in [SeawolfExprParser.ID]:
                localctx = SeawolfExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(SeawolfExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SeawolfExprParser.MulDivContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SeawolfExprParser.MUL or _la==SeawolfExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = SeawolfExprParser.ModulusContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 33
                        localctx.op = self.match(SeawolfExprParser.MOD)
                        self.state = 34
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = SeawolfExprParser.ExponentContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 36
                        localctx.op = self.match(SeawolfExprParser.EXP)
                        self.state = 37
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = SeawolfExprParser.FloorDivisionContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 39
                        localctx.op = self.match(SeawolfExprParser.FLRDIV)
                        self.state = 40
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = SeawolfExprParser.AddSubContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SeawolfExprParser.ADD or _la==SeawolfExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = SeawolfExprParser.LogicalContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SeawolfExprParser.LESS) | (1 << SeawolfExprParser.LESSEQ) | (1 << SeawolfExprParser.GRT) | (1 << SeawolfExprParser.GRTEQ) | (1 << SeawolfExprParser.EQUAL) | (1 << SeawolfExprParser.NOTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(8)
                        pass

                    elif la_ == 7:
                        localctx = SeawolfExprParser.BinaryAndContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        localctx.op = self.match(SeawolfExprParser.AND)
                        self.state = 49
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = SeawolfExprParser.BinaryOrContext(self, SeawolfExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 51
                        localctx.op = self.match(SeawolfExprParser.OR)
                        self.state = 52
                        self.expr(5)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         





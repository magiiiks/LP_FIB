# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,44,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        29,8,1,5,1,31,8,1,10,1,12,1,34,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,42,
        8,2,1,2,0,1,2,3,0,2,4,0,1,1,0,3,4,48,0,6,1,0,0,0,2,20,1,0,0,0,4,
        41,1,0,0,0,6,7,3,2,1,0,7,1,1,0,0,0,8,9,6,1,-1,0,9,10,5,1,0,0,10,
        11,3,2,1,0,11,12,5,2,0,0,12,21,1,0,0,0,13,14,5,5,0,0,14,15,5,10,
        0,0,15,16,5,6,0,0,16,21,3,2,1,5,17,21,7,0,0,0,18,21,5,8,0,0,19,21,
        5,10,0,0,20,8,1,0,0,0,20,13,1,0,0,0,20,17,1,0,0,0,20,18,1,0,0,0,
        20,19,1,0,0,0,21,32,1,0,0,0,22,23,10,6,0,0,23,31,3,2,1,7,24,25,10,
        4,0,0,25,28,5,7,0,0,26,29,3,4,2,0,27,29,5,9,0,0,28,26,1,0,0,0,28,
        27,1,0,0,0,29,31,1,0,0,0,30,22,1,0,0,0,30,24,1,0,0,0,31,34,1,0,0,
        0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,1,0,0,0,34,32,1,0,0,0,35,36,5,
        9,0,0,36,37,5,6,0,0,37,42,3,4,2,0,38,39,5,9,0,0,39,40,5,6,0,0,40,
        42,5,9,0,0,41,35,1,0,0,0,41,38,1,0,0,0,42,5,1,0,0,0,5,20,28,30,32,
        41
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'(+)'", "'(-)'", "'\\'", 
                     "'->'", "'::'" ]

    symbolicNames = [ "<INVALID>", "OPAR", "CPAR", "PLUS", "MINUS", "BARRA", 
                      "FLEXA", "PUNTS", "NUM", "TIPUS", "ID", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_funtipus = 2

    ruleNames =  [ "root", "expr", "funtipus" ]

    EOF = Token.EOF
    OPAR=1
    CPAR=2
    PLUS=3
    MINUS=4
    BARRA=5
    FLEXA=6
    PUNTS=7
    NUM=8
    TIPUS=9
    ID=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AbstracContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BARRA(self):
            return self.getToken(hmParser.BARRA, 0)
        def ID(self):
            return self.getToken(hmParser.ID, 0)
        def FLEXA(self):
            return self.getToken(hmParser.FLEXA, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstrac" ):
                return visitor.visitAbstrac(self)
            else:
                return visitor.visitChildren(self)


    class IdentificationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentification" ):
                return visitor.visitIdentification(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication" ):
                return visitor.visitImplication(self)
            else:
                return visitor.visitChildren(self)


    class TipusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)

        def PUNTS(self):
            return self.getToken(hmParser.PUNTS, 0)
        def funtipus(self):
            return self.getTypedRuleContext(hmParser.FuntipusContext,0)

        def TIPUS(self):
            return self.getToken(hmParser.TIPUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipus" ):
                return visitor.visitTipus(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(hmParser.OPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)

        def CPAR(self):
            return self.getToken(hmParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class OperatorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(hmParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(hmParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = hmParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.match(hmParser.OPAR)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(hmParser.CPAR)
                pass
            elif token in [5]:
                localctx = hmParser.AbstracContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(hmParser.BARRA)
                self.state = 14
                self.match(hmParser.ID)
                self.state = 15
                self.match(hmParser.FLEXA)
                self.state = 16
                self.expr(5)
                pass
            elif token in [3, 4]:
                localctx = hmParser.OperatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [8]:
                localctx = hmParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(hmParser.NUM)
                pass
            elif token in [10]:
                localctx = hmParser.IdentificationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(hmParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = hmParser.ImplicationContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 23
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = hmParser.TipusContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 25
                        self.match(hmParser.PUNTS)
                        self.state = 28
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                        if la_ == 1:
                            self.state = 26
                            self.funtipus()
                            pass

                        elif la_ == 2:
                            self.state = 27
                            self.match(hmParser.TIPUS)
                            pass


                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuntipusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_funtipus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FinTipusContext(FuntipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.FuntipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPUS(self, i:int=None):
            if i is None:
                return self.getTokens(hmParser.TIPUS)
            else:
                return self.getToken(hmParser.TIPUS, i)
        def FLEXA(self):
            return self.getToken(hmParser.FLEXA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinTipus" ):
                return visitor.visitFinTipus(self)
            else:
                return visitor.visitChildren(self)


    class FunTipusContext(FuntipusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.FuntipusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPUS(self):
            return self.getToken(hmParser.TIPUS, 0)
        def FLEXA(self):
            return self.getToken(hmParser.FLEXA, 0)
        def funtipus(self):
            return self.getTypedRuleContext(hmParser.FuntipusContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunTipus" ):
                return visitor.visitFunTipus(self)
            else:
                return visitor.visitChildren(self)



    def funtipus(self):

        localctx = hmParser.FuntipusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funtipus)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = hmParser.FunTipusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(hmParser.TIPUS)
                self.state = 36
                self.match(hmParser.FLEXA)
                self.state = 37
                self.funtipus()
                pass

            elif la_ == 2:
                localctx = hmParser.FinTipusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(hmParser.TIPUS)
                self.state = 39
                self.match(hmParser.FLEXA)
                self.state = 40
                self.match(hmParser.TIPUS)
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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         





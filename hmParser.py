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
        4,1,8,22,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,0,0,2,0,2,0,1,1,0,3,4,23,0,4,
        1,0,0,0,2,19,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,5,1,0,0,7,8,3,2,
        1,0,8,9,5,2,0,0,9,20,1,0,0,0,10,11,7,0,0,0,11,12,3,2,1,0,12,13,3,
        2,1,0,13,20,1,0,0,0,14,15,5,7,0,0,15,16,5,5,0,0,16,20,3,2,1,0,17,
        20,5,6,0,0,18,20,5,7,0,0,19,6,1,0,0,0,19,10,1,0,0,0,19,14,1,0,0,
        0,19,17,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,1,19
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'->'" ]

    symbolicNames = [ "<INVALID>", "OPAR", "CPAR", "PLUS", "MINUS", "FLEXA", 
                      "NUM", "ID", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    OPAR=1
    CPAR=2
    PLUS=3
    MINUS=4
    FLEXA=5
    NUM=6
    ID=7
    WS=8

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




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
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

        def OPAR(self):
            return self.getToken(hmParser.OPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def CPAR(self):
            return self.getToken(hmParser.CPAR, 0)

        def PLUS(self):
            return self.getToken(hmParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(hmParser.MINUS, 0)

        def ID(self):
            return self.getToken(hmParser.ID, 0)

        def FLEXA(self):
            return self.getToken(hmParser.FLEXA, 0)

        def NUM(self):
            return self.getToken(hmParser.NUM, 0)

        def getRuleIndex(self):
            return hmParser.RULE_expr




    def expr(self):

        localctx = hmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(hmParser.OPAR)
                self.state = 7
                self.expr()
                self.state = 8
                self.match(hmParser.CPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 11
                self.expr()
                self.state = 12
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(hmParser.ID)
                self.state = 15
                self.match(hmParser.FLEXA)
                self.state = 16
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(hmParser.NUM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 18
                self.match(hmParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






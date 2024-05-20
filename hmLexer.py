# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,64,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,4,7,
        45,8,7,11,7,12,7,46,1,8,1,8,1,9,1,9,5,9,53,8,9,10,9,12,9,56,9,9,
        1,10,4,10,59,8,10,11,10,12,10,60,1,10,1,10,0,0,11,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,3,2,0,65,90,97,122,4,0,
        48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,66,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,
        0,0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,31,1,0,0,0,9,35,1,0,0,0,11,37,
        1,0,0,0,13,40,1,0,0,0,15,44,1,0,0,0,17,48,1,0,0,0,19,50,1,0,0,0,
        21,58,1,0,0,0,23,24,5,40,0,0,24,2,1,0,0,0,25,26,5,41,0,0,26,4,1,
        0,0,0,27,28,5,40,0,0,28,29,5,43,0,0,29,30,5,41,0,0,30,6,1,0,0,0,
        31,32,5,40,0,0,32,33,5,45,0,0,33,34,5,41,0,0,34,8,1,0,0,0,35,36,
        5,92,0,0,36,10,1,0,0,0,37,38,5,45,0,0,38,39,5,62,0,0,39,12,1,0,0,
        0,40,41,5,58,0,0,41,42,5,58,0,0,42,14,1,0,0,0,43,45,2,48,57,0,44,
        43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,16,1,0,0,
        0,48,49,2,65,90,0,49,18,1,0,0,0,50,54,7,0,0,0,51,53,7,1,0,0,52,51,
        1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,20,1,0,0,0,
        56,54,1,0,0,0,57,59,7,2,0,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,
        0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,6,10,0,0,63,22,1,0,0,0,4,
        0,46,54,60,1,6,0,0
    ]

class hmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPAR = 1
    CPAR = 2
    PLUS = 3
    MINUS = 4
    BARRA = 5
    FLEXA = 6
    PUNTS = 7
    NUM = 8
    TIPUS = 9
    ID = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'(+)'", "'(-)'", "'\\'", "'->'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "OPAR", "CPAR", "PLUS", "MINUS", "BARRA", "FLEXA", "PUNTS", 
            "NUM", "TIPUS", "ID", "WS" ]

    ruleNames = [ "OPAR", "CPAR", "PLUS", "MINUS", "BARRA", "FLEXA", "PUNTS", 
                  "NUM", "TIPUS", "ID", "WS" ]

    grammarFileName = "hm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



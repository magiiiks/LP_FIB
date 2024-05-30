# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#abstrac.
    def visitAbstrac(self, ctx:hmParser.AbstracContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#identification.
    def visitIdentification(self, ctx:hmParser.IdentificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#implication.
    def visitImplication(self, ctx:hmParser.ImplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#Tipus.
    def visitTipus(self, ctx:hmParser.TipusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx:hmParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#value.
    def visitValue(self, ctx:hmParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#operator.
    def visitOperator(self, ctx:hmParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#funTipus.
    def visitFunTipus(self, ctx:hmParser.FunTipusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#finTipus.
    def visitFinTipus(self, ctx:hmParser.FinTipusContext):
        return self.visitChildren(ctx)



del hmParser
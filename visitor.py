if "." in __name__:
    from .hmParser import hmParser
    from .hmVisitor import hmVisitor
else:
    from hmParser import hmParser
    from hmVisitor import hmVisitor
import graphviz
from dataclasses import dataclass
from typing import Union

#declaracions del tree
@dataclass
class Node:
    left: 'Node'
    right: 'Node'
    val: str


@dataclass
class Tipus:
    simbol: str
    tipus: str



class treeVisitor(hmVisitor):
    def __init__(self, entryProc = 'main', entryParams = [], taulaS = [], taulaT = []):
        self.entryProc = entryProc
        self.entryParams = entryParams
        self.taulaTipus = taulaT
        self.taulaSimbols = taulaS
        self.taulaSimbols2 = []
        self.taulaTipus2 = []
        self.valtipus = 'a'

    def expr_to_dot(self, tree):  #transforma BinTree a Dot
        dot = graphviz.Graph()
    
        def add_nodes_edges(expr, parent=None):
            if isinstance(expr, Node):
                if(expr.val in self.taulaSimbols):
                    i = self.taulaSimbols.index(expr.val)
                    dot.node(str(id(expr)), expr.val+'\n'+self.taulaTipus[i])
                else:
                    if(expr.val in self.taulaSimbols2 and expr.val != "@"):
                        i = self.taulaSimbols2.index(expr.val)
                        dot.node(str(id(expr)), expr.val+'\n'+self.taulaTipus2[i])
                    else:
                        dot.node(str(id(expr)), expr.val+'\n'+self.valtipus)
                        self.taulaSimbols2.append(expr.val)
                        self.taulaTipus2.append(self.valtipus)
                        self.valtipus = chr(ord(self.valtipus) +1)
                if parent:
                    dot.edge(str(id(parent)), str(id(expr)))
                add_nodes_edges(expr.left, expr)
                add_nodes_edges(expr.right, expr)
    
        add_nodes_edges(tree)
        return dot
    
    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        n = self.visitChildren(ctx)      
        return self.expr_to_dot(n), self.taulaTipus, self.taulaSimbols


    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx:hmParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#arithmetic.
    def visitArithmetic(self, ctx:hmParser.ArithmeticContext):
        [operador, expr1, expr2] = list(ctx.getChildren())
        op = Node(None, None, operador.getText())
        e1 = self.visit(expr1)
        e2 = self.visit(expr2)

        n1 = Node(op, e1, "@")
        n2 = Node(n1, e2, "@")
        return n2
    
    # Visit a parse tree produced by hmParser#unary.
    def visitUnary(self, ctx:hmParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#implication.
    def visitImplication(self, ctx:hmParser.ImplicationContext):
        [expr1, operador, expr2] = list(ctx.getChildren())
        e1 = self.visit(expr1)
        e2 = self.visit(expr2)
        return Node(e1, e2, "λ")  

    # Visit a parse tree produced by hmParser#numTipus.
    def visitNumTipus(self, ctx:hmParser.NumTipusContext):
        [expr1, punts, tipus] = list(ctx.getChildren())
        if(not expr1.getText() in self.taulaSimbols):
            self.taulaTipus.append(tipus.getText())
            self.taulaSimbols.append(expr1.getText())
        return     
    
    # Visit a parse tree produced by hmParser#funTipus.
    def visitFunTipus(self, ctx:hmParser.FunTipusContext):
        [expr1, punts, t1, f1, t2, f2, t3] = list(ctx.getChildren())
        if(not expr1.getText() in self.taulaSimbols):
            self.taulaTipus.append(str("(" + t1.getText() + " -> (" + t2.getText() + " -> " + t3.getText() + "))"))
            self.taulaSimbols.append(expr1.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#value.
    def visitValue(self, ctx:hmParser.ValueContext):
        return Node(None, None, ctx.getText()) 
    
    # Visit a parse tree produced by hmParser#abstrac.
    def visitAbstrac(self, ctx:hmParser.AbstracContext):
        [barra, expr1] = list(ctx.getChildren())
        e1 = self.visit(expr1)
        return Node(None, None, expr1.getText()) 

    # Visit a parse tree produced by hmParser#identification.
    def visitIdentification(self, ctx:hmParser.IdentificationContext):
        return Node(None, None, ctx.getText()) 



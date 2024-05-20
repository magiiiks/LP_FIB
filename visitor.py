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
class Num:
    value: int

@dataclass
class Node:
    left: 'Expr'
    right: 'Expr'
    val: str

Expr = Union[Num, Node]

@dataclass
class Tipus:
    simbol: str
    tipus: str



class treeVisitor(hmVisitor):
    def __init__(self, entryProc = 'main', entryParams = []):
        self.entryProc = entryProc
        self.entryParams = entryParams
        self.taulaTipus = []

    def expr_to_dot(self, tree):  #transforma BinTree a Dot
        dot = graphviz.Graph()
    
        def add_nodes_edges(expr, parent=None):
            if isinstance(expr, Num):
                dot.node(str(id(expr)), str(expr.value))
                if parent:
                    dot.edge(str(id(parent)), str(id(expr)))
            elif isinstance(expr, Node):
                dot.node(str(id(expr)), expr.val)
                if parent:
                    dot.edge(str(id(parent)), str(id(expr)))
                add_nodes_edges(expr.left, expr)
                add_nodes_edges(expr.right, expr)
    
        add_nodes_edges(tree)
        return dot

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        n = self.visitChildren(ctx)      
        return self.expr_to_dot(n), self.taulaTipus


    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx:hmParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#arithmetic.
    def visitArithmetic(self, ctx:hmParser.ArithmeticContext):
        [operador, expr1, expr2] = list(ctx.getChildren())
        self.nivell += 1
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
        self.taulaTipus.append(Tipus(expr1.getText(), tipus.getText()))
        return     
    
    # Visit a parse tree produced by hmParser#funTipus.
    def visitFunTipus(self, ctx:hmParser.FunTipusContext):
        [expr1, punts, t1, f1, t2, f2, t3] = list(ctx.getChildren())
        self.taulaTipus.append(Tipus(expr1.getText(), "(" + t1.getText() + " -> (" + t2.getText() + " -> " + t3.getText() + "))"))
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



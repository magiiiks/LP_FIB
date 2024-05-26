if "." in __name__:
    from .hmParser import hmParser
    from .hmVisitor import hmVisitor
else:
    from hmParser import hmParser
    from hmVisitor import hmVisitor
import graphviz
from dataclasses import dataclass
from typing import Union
import copy

# declaracions del tree


@dataclass
class Node:
    left: 'Node'
    right: 'Node'
    val: str
    tipus: str


class treeVisitor(hmVisitor):
    def __init__(self, entryProc='main', entryParams=[], taulaS=[], taulaT=[]):
        self.entryProc = entryProc
        self.entryParams = entryParams
        self.taulaTipus = taulaT
        self.taulaSimbols = taulaS
        self.taulaSimbols2 = []
        self.taulaTipus2 = []
        self.valtipus = 'a'
        self.taulaInferencia1 = []
        self.taulaInferencia2 = []

    def expr_to_dot(self, tree):  # transforma BinTree a Dot
        dot = graphviz.Graph()

        def add_nodes_edges(expr, parent=None):
            if isinstance(expr, Node):
                dot.node(str(id(expr)), expr.val+'\n'+str(expr.tipus))
                if parent:
                    dot.edge(str(id(parent)), str(id(expr)))
                add_nodes_edges(expr.left, expr)
                add_nodes_edges(expr.right, expr)

        add_nodes_edges(tree)
        return dot

    def posarTipus(self, tree):
        if isinstance(tree, Node):
            if (tree.val in self.taulaSimbols):
                i = self.taulaSimbols.index(tree.val)
                tree.tipus = self.taulaTipus[i]
            else:
                if (tree.val in self.taulaSimbols2 and tree.val != "@"):
                    i = self.taulaSimbols2.index(tree.val)
                    tree.tipus = self.taulaTipus2
                else:
                    tree.tipus = self.valtipus
                    self.taulaSimbols2.append(tree.val)
                    self.taulaTipus2.append(self.valtipus)
                    self.valtipus = chr(ord(self.valtipus) + 1)
            self.posarTipus(tree.left)
            self.posarTipus(tree.right)
        return tree

    def inferenciaTipus(self, tree):
        if isinstance(tree, Node):
            if (tree.left == None and tree.right == None):
                return tree
            else:
                tl = self.inferenciaTipus(tree.left)
                tr = self.inferenciaTipus(tree.right)
                llarg = False
                if (isinstance(tl, Node) and isinstance(tr, Node)):
                    if (tl.tipus == None):
                        return tl
                    if (tr.tipus == None):
                        return tr
                    if (len(tl.tipus) > 8):
                        text = tl.tipus.split()
                        [t1, flexa, t2, flexa, t3] = list(text)
                        llarg = True
                        t1 = t1[1]
                        t2 = t2[1]
                        t3 = t3[0]
                    elif (len(tl.tipus) > 1):
                        text = tl.tipus.split()
                        [t1, flexa, t2] = list(text)
                        t1 = t1[1]
                        t2 = t2[0]
                    else:
                        t1 = tl.tipus

                    if (t1 == tr.tipus):
                        self.taulaInferencia1.append(tree.tipus)
                        if (llarg):
                            tree.tipus = str("("+t2 + " -> " + t3+")")
                        else:
                            tree.tipus = tr.tipus
                        self.taulaInferencia2.append(tree.tipus)
                        return tree
                    else:
                        if (tr.tipus.islower()):
                            self.taulaInferencia1.append(tree.tipus)
                            self.taulaInferencia1.append(tr.tipus)
                            tree.tipus = t1
                            tr.tipus = t1
                            self.taulaInferencia2.append(tree.tipus)
                            self.taulaInferencia2.append(tr.tipus)
                            return tree
                        return Node(None, None, "Type error: " + tl.tipus + " vs " + tr.tipus, None)

    # Visit a parse tree produced by hmParser#root.

    def visitRoot(self, ctx: hmParser.RootContext):
        n = self.visitChildren(ctx)
        n = self.posarTipus(n)
        t = copy.deepcopy(n)
        t = self.inferenciaTipus(t)
        return self.expr_to_dot(n), self.expr_to_dot(t), self.taulaTipus, self.taulaSimbols, self.taulaInferencia1, self.taulaInferencia2

    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx: hmParser.ParenthesisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by hmParser#arithmetic.
    def visitArithmetic(self, ctx: hmParser.ArithmeticContext):
        [operador, expr1, expr2] = list(ctx.getChildren())
        op = Node(None, None, operador.getText(), None)
        e1 = self.visit(expr1)
        e2 = self.visit(expr2)

        n1 = Node(op, e1, "@", None)
        n2 = Node(n1, e2, "@", None)
        return n2

    # Visit a parse tree produced by hmParser#unary.
    def visitUnary(self, ctx: hmParser.UnaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by hmParser#implication.
    def visitImplication(self, ctx: hmParser.ImplicationContext):
        [expr1, operador, expr2] = list(ctx.getChildren())
        e1 = self.visit(expr1)
        e2 = self.visit(expr2)
        return Node(e1, e2, "λ", None)

    # Visit a parse tree produced by hmParser#numTipus.
    def visitNumTipus(self, ctx: hmParser.NumTipusContext):
        [expr1, punts, tipus] = list(ctx.getChildren())
        if (not expr1.getText() in self.taulaSimbols):
            self.taulaTipus.append(tipus.getText())
            self.taulaSimbols.append(expr1.getText())
        return

    # Visit a parse tree produced by hmParser#funTipus.
    def visitFunTipus(self, ctx: hmParser.FunTipusContext):
        [expr1, punts, t1, f1, t2, f2, t3] = list(ctx.getChildren())
        if (not expr1.getText() in self.taulaSimbols):
            self.taulaTipus.append(
                str("(" + t1.getText() + " -> (" + t2.getText() + " -> " + t3.getText() + "))"))
            self.taulaSimbols.append(expr1.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by hmParser#value.
    def visitValue(self, ctx: hmParser.ValueContext):
        return Node(None, None, ctx.getText(), None)

    # Visit a parse tree produced by hmParser#abstrac.
    def visitAbstrac(self, ctx: hmParser.AbstracContext):
        [barra, expr1] = list(ctx.getChildren())
        e1 = self.visit(expr1)
        return Node(None, None, expr1.getText(), None)

    # Visit a parse tree produced by hmParser#identification.
    def visitIdentification(self, ctx: hmParser.IdentificationContext):
        return Node(None, None, ctx.getText(), None)

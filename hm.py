import streamlit as st
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser

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


# declaracions de la taula de simbols
if 'taulaSimbols' not in st.session_state:
    st.session_state.taulaSimbols = []

if 'taulaTipus' not in st.session_state:
    st.session_state.taulaTipus = []


class treeVisitor(hmVisitor):
    def __init__(self, taulaS=[], taulaT=[]):
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

    def posarTipus(self, tree):  # posa els tipus en el arbre
        if isinstance(tree, Node):
            if (tree.val in self.taulaSimbols):
                i = self.taulaSimbols.index(tree.val)
                tree.tipus = self.taulaTipus[i]
            else:
                if (tree.val in self.taulaSimbols2 and tree.val != "@"):
                    i = self.taulaSimbols2.index(tree.val)
                    tree.tipus = self.taulaTipus2[i]
                else:
                    tree.tipus = self.valtipus
                    self.taulaSimbols2.append(tree.val)
                    self.taulaTipus2.append(self.valtipus)
                    self.valtipus = chr(ord(self.valtipus) + 1)
            self.posarTipus(tree.left)
            self.posarTipus(tree.right)
        return tree

    def inferenciaTipus(self, tree):  # fa la inferencia de tipus
        if isinstance(tree, Node):
            if (tree.left == None and tree.right == None):
                if (tree.tipus in self.taulaInferencia1):
                    i = self.taulaInferencia1.index(tree.tipus)
                    tree.tipus = self.taulaInferencia2[i]
                return tree
            elif (tree.val == "λ"):
                tr = self.inferenciaTipus(tree.right)
                tl = self.inferenciaTipus(tree.left)
                nt = str("(" + tl.tipus + " -> " + tr.tipus + ")")
                self.taulaInferencia1.append(tree.tipus)
                self.taulaInferencia2.append(nt)
                tree.tipus = nt
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

    # Visit a parse tree produced by hmParser#abstrac.
    def visitAbstrac(self, ctx: hmParser.AbstracContext):
        [barra, id, flexa, expr] = list(ctx.getChildren())
        e = self.visit(expr)
        i = Node(None, None, id.getText(), None)
        return Node(i, e, "λ", None)

    # Visit a parse tree produced by hmParser#identification.
    def visitIdentification(self, ctx: hmParser.IdentificationContext):
        return Node(None, None, ctx.getText(), None)

    # Visit a parse tree produced by hmParser#implication.
    def visitImplication(self, ctx: hmParser.ImplicationContext):
        [expr1, expr2] = list(ctx.getChildren())
        e1 = self.visit(expr1)
        e2 = self.visit(expr2)

        return Node(e1, e2, "@", None)

    # Visit a parse tree produced by hmParser#Tipus.
    def visitTipus(self, ctx: hmParser.TipusContext):
        if (ctx.TIPUS()):
            [expr1, punts, tipus] = list(ctx.getChildren())
            if (not expr1.getText() in self.taulaSimbols):
                self.taulaTipus.append(tipus.getText())
                self.taulaSimbols.append(expr1.getText())

        else:
            [expr1, punts, tipus] = list(ctx.getChildren())
            t = self.visit(tipus)
            if (not expr1.getText() in self.taulaSimbols):
                self.taulaTipus.append(t)
                self.taulaSimbols.append(expr1.getText())
        return

    # Visit a parse tree produced by hmParser#parenthesis.
    def visitParenthesis(self, ctx: hmParser.ParenthesisContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by hmParser#value.
    def visitValue(self, ctx: hmParser.ValueContext):
        return Node(None, None, ctx.getText(), None)

    # Visit a parse tree produced by hmParser#operator.
    def visitOperator(self, ctx: hmParser.OperatorContext):
        return Node(None, None, ctx.getText(), None)

    # Visit a parse tree produced by hmParser#funTipus.
    def visitFunTipus(self, ctx: hmParser.FunTipusContext):
        t = self.visit(ctx.funtipus())
        return str("("+ctx.TIPUS().getText()+" -> "+t+")")

    # Visit a parse tree produced by hmParser#finTipus.
    def visitFinTipus(self, ctx: hmParser.FinTipusContext):
        return str("("+ctx.TIPUS(0).getText()+" -> "+ctx.TIPUS(1).getText()+")")


st.title("Analitzador de tipus HinNer")

tin = st.text_input("Expressió:")
if (st.button("fer")):
    input_stream = InputStream(tin)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)

    tree = parser.root()
    st.write(parser.getNumberOfSyntaxErrors(), 'Errors de sintaxi.')
    visitor = treeVisitor(taulaS=st.session_state.taulaSimbols,
                          taulaT=st.session_state.taulaTipus)
    dot, dotTipus, taulaT, taulaS, taulaI1, taulaI2 = visitor.visit(tree)
    st.session_state.taulaSimbols = taulaS
    st.session_state.taulaTipus = taulaT
    if (len(st.session_state.taulaSimbols) > 0):  # nomes mostrarem la taula si te tipus emmagatzemats
        st.write("Taula de símbols:")
        tabla = [[st.session_state.taulaSimbols[i], st.session_state.taulaTipus[i]]
                 for i in range(len(st.session_state.taulaSimbols))]
        st.table(tabla)
    st.graphviz_chart(dot)
    # nomes farem inferència de tipus si tinc tipus emmagatzemats
    if (len(st.session_state.taulaSimbols) > 0):
        st.graphviz_chart(dotTipus)
        if (len(taulaI1) > 0):  # nomes mostrarem la taula si te tipus emmagatzemats
            tabla1 = [[taulaI1[i], taulaI2[i]]
                      for i in range(len(taulaI1)-1, -1, -1)]
            st.table(tabla1)

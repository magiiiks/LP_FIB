import streamlit as st
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from visitor import treeVisitor

if 'taulaSimbols' not in st.session_state:
    st.session_state.taulaSimbols = []

if 'taulaTipus' not in st.session_state:
    st.session_state.taulaTipus = []

st.title("Analitzador de tipus HinNer")

tin = st.text_input("Expressió:")
if (st.button("fer")):
    input_stream = InputStream(tin)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)

    tree = parser.root()
    st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    visitor = treeVisitor(taulaS=st.session_state.taulaSimbols,
                          taulaT=st.session_state.taulaTipus)
    dot, dotTipus, taulaT, taulaS, taulaI1, taulaI2 = visitor.visit(tree)
    st.session_state.taulaSimbols = taulaS
    st.session_state.taulaTipus = taulaT
    tabla = [[st.session_state.taulaSimbols[i], st.session_state.taulaTipus[i]]
             for i in range(len(st.session_state.taulaSimbols))]
    st.table(tabla)
    st.graphviz_chart(dot)
    st.graphviz_chart(dotTipus)
    if (len(taulaI1) > 0):
        tabla1 = [[taulaI1[i], taulaI2[i]]
                  for i in range(len(taulaI1))]
        st.table(tabla1)

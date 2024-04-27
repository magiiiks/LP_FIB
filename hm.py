import streamlit as st
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor


st.title("Analitzador de tipus HinNer")

tin = st.text_input("Expressió:")
if (st.button("fer")):
    input_stream = InputStream(tin)
    lexer = hmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hmParser(token_stream)
    tree = parser.root()
    st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    st.write(tree.toStringTree(recog=parser))
    #dot = hmVisitor()
    #st.graphviz_chart(dot)
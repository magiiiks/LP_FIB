import graphviz

class hmVisitor():
    

    def __init__(self) -> graphviz.Digraph:
        dot = graphviz.Digraph()
        dot.edge('run', 'intr')
        dot.edge('intr', 'runbl')
        dot.edge('runbl', 'run')
        dot.edge('run', 'kernel')
        dot.edge('kernel', 'zombie')
        dot.edge('kernel', 'sleep')
        dot.edge('kernel', 'runmem')
        dot.edge('sleep', 'swap')
        dot.edge('swap', 'runswap')
        dot.edge('runswap', 'new')
        dot.edge('runswap', 'runmem')
        dot.edge('new', 'runmem')
        return dot
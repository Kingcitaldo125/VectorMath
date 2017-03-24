from graphviz import Digraph

dot = Digraph(comment='The Thing')

dot.node('A', 'King')
dot.node('B', 'Queen')
dot.node('C', 'Prince')

dot.edges(['AB','AC','BC'])
print(dot.source)
dot.render()

# wk2assignment.py
# Author: Neil Acampa
# Date:   09/07/16
# Course: IS620
# Function: Create a basic graph and save in ipython notebook

# Works with graphlab but cannot get graphlab to work in ipython notebook


from graphlab import SGraph, Vertex, Edge
from graphlab import SFrame
g = SGraph()

vert_data = [Vertex(1, attr={'name': 'Alice'}),
         Vertex(2, attr={'name':  'Beth'}),
         Vertex(3, attr={'name': 'Cindy'}),
         Vertex(4, attr={'name':  'Dana'}),
         Vertex(5, attr={'name':  'Elsa'}),
         Vertex(6, attr={'name': 'Frida'}),
         Vertex(7, attr={'name':  'Gina'}),
         Vertex(8, attr={'name': 'Helena'}),
         Vertex(9, attr={'name':    'Ida'}),
         Vertex(10,attr={'name':   'Jena'})]


g = g.add_vertices(vert_data)

g = g.add_edges(Edge(1, 2))
g = g.add_edges(Edge(1, 3))
g = g.add_edges(Edge(1, 4))
g = g.add_edges(Edge(1, 6))
g = g.add_edges(Edge(2, 1))
g = g.add_edges(Edge(2, 4))
g = g.add_edges(Edge(2, 5))
g = g.add_edges(Edge(2, 7))
g = g.add_edges(Edge(3, 1))
g = g.add_edges(Edge(3, 4))
g = g.add_edges(Edge(3, 6))
g = g.add_edges(Edge(4, 1))
g = g.add_edges(Edge(4, 2))
g = g.add_edges(Edge(4, 3))
g = g.add_edges(Edge(4, 5))
g = g.add_edges(Edge(4, 6))
g = g.add_edges(Edge(4, 7))
g = g.add_edges(Edge(5, 2))
g = g.add_edges(Edge(5, 4))
g = g.add_edges(Edge(5, 7))
g = g.add_edges(Edge(6, 1))
g = g.add_edges(Edge(6, 3))
g = g.add_edges(Edge(6, 4))
g = g.add_edges(Edge(6, 7))
g = g.add_edges(Edge(6, 8))
g = g.add_edges(Edge(7, 2))
g = g.add_edges(Edge(7, 4))
g = g.add_edges(Edge(7, 5))
g = g.add_edges(Edge(7, 6))
g = g.add_edges(Edge(7, 8))
g = g.add_edges(Edge(8, 6))
g = g.add_edges(Edge(8, 7))
g = g.add_edges(Edge(8, 9))
g = g.add_edges(Edge(9, 8))
g = g.add_edges(Edge(9, 10))
g = g.add_edges(Edge(10,9))

print g

g.show(vlabel='name', arrows=True)






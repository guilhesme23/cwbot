import pytest
from graph.node import Node
from graph.graphw import GraphW
from itertools import islice, count

@pytest.fixture
def w_nodes():
    return list(islice(map(Node, count(start=1)), 5))

@pytest.fixture
def w_graph(w_nodes):
    n1, n2, n3, n4, n5 = w_nodes
    g = GraphW()
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)
    g.add_node(n5)
    return g

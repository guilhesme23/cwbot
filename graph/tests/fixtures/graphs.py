import pytest
from graph.graph import Graph
from graph.node import Node
from itertools import count, islice

@pytest.fixture
def simple_nodes():
    return list(islice(map(Node, count(start=1)), 5))

@pytest.fixture
def simple_g(simple_nodes):
    n1, n2, n3, n4, n5 = simple_nodes
    _g = Graph()
    _g.add_node(n1, [n2, n3])
    _g.add_node(n2, [n1, n4])
    _g.add_node(n3, [n1, n5])
    _g.add_node(n4, [n2, n5])
    _g.add_node(n5, [n3, n2])
    return _g


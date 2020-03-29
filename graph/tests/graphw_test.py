import pytest
from graph.graphw import GraphW
from graph.node import Node
from itertools import count, islice

class TestGraphW:
    def test_add_node(self, w_graph):
        n6 = Node(6)
        w_graph.add_node(n6)
        assert len(w_graph.nodes) == 6

    def test_unique_nodes(self, w_graph, w_nodes):
        n1, *_ = w_nodes
        w_graph.add_node(n1)
        assert len(w_graph.nodes) == 5
    
    def test_get_idx(self, w_graph):
        node = w_graph.get_by_idx(2)
        assert isinstance(node, Node)
    
    def test_add_edges(self, w_graph):
        n6 = Node(6)
        w_graph.add_node(n6)
        w_graph.add_edge(5, 6)
        n5 = w_graph.get_by_idx(5)
        assert n6 in w_graph[n5]
        assert n5 not in w_graph[n6]
    
    def test_add_w_edges(self, w_graph):
        n5 = w_graph.get_by_idx(5)
        n6 = Node(6)
        w_graph.add_edge(n6, n5, 3)
        assert w_graph.weights[(n6, n5)] == 3

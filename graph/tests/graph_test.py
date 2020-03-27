import pytest
from graph.graph import Graph
from graph.node import Node
from itertools import count, islice

class TestNode:
    def test_get_by_idx(self, simple_g, simple_nodes):
        n1, *_ = simple_nodes
        assert simple_g.get_by_idx(1) == n1
    
    def test_get_idx_none(self, simple_g):
        assert simple_g.get_by_idx(50) == None
    
    def test_graph_is_subscriptable(self, simple_g, simple_nodes):
        n1, *_  = simple_nodes
        simple_g[n1]
    
    def test_all_nodes_stored(self, simple_g):
        n6 = Node(6)
        simple_g.add_node(n6, [])
        assert len(simple_g.nodes) == 6
    
    def test_bidirectional_links(self, simple_g, simple_nodes):
        n6 = Node(6)
        *_, n5 = simple_nodes
        simple_g.add_node(n6, [n5])
        assert n6 in simple_g[n5]
    
    def test_bfs_path_builder(self, simple_g, simple_nodes):
        n1, n2, n3, n4, n5 = simple_nodes
        path_table = {
            n5: n3,
            n3: n1
        }
        assert simple_g._gen_bfs_path(n1, n5, path_table) == [n1, n3, n5]
    
    def test_bfs_search(self, simple_g, simple_nodes):
        n1, n2, n3, n4, n5 = simple_nodes
        connected, layers, path = simple_g.bfs(n1, n5)
        assert len(connected) == 5
        assert path == [n1, n2, n5]
        assert len(layers) == 3
    
    def test_dfs_search(self, simple_g):
        res = simple_g.dfs(3)
        print(res)
        assert len(res) == 5
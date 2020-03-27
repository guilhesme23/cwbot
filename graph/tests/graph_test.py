import pytest
from graph.graph import Graph
from graph.node import Node
from itertools import count, islice

class TestNode:
    @pytest.fixture
    def init_nodes(self):
        return list(islice(map(Node, count(start=1)), 5))

    @pytest.fixture
    def g(self, init_nodes):
        n1, n2, n3, n4, n5 = init_nodes
        _g = Graph()
        _g.add_node(n1, [n2, n3])
        _g.add_node(n2, [n1, n4])
        _g.add_node(n3, [n1, n5])
        _g.add_node(n4, [n2, n5])
        _g.add_node(n5, [n3, n2])
        return _g

    def test_get_by_idx(self, g, init_nodes):
        n1, *_ = init_nodes
        assert g.get_by_idx(1) == n1
    
    def test_get_idx_none(self, g):
        assert g.get_by_idx(50) == None
    
    def test_graph_is_subscriptable(self, g, init_nodes):
        n1, *_  = init_nodes
        g[n1]
    
    def test_all_nodes_stored(self, g):
        n6 = Node(6)
        g.add_node(n6, [])
        assert len(g.nodes) == 6
    
    def test_bidirectional_links(self, g, init_nodes):
        n6 = Node(6)
        *_, n5 = init_nodes
        g.add_node(n6, [n5])
        assert n6 in g[n5]
    
    def test_bfs_path_builder(self, g, init_nodes):
        n1, n2, n3, n4, n5 = init_nodes
        path_table = {
            n5: n3,
            n3: n1
        }
        assert g._gen_bfs_path(n1, n5, path_table) == [n1, n3, n5]
    
    def test_bfs_search(self, g, init_nodes):
        n1, n2, n3, n4, n5 = init_nodes
        connected, layers, path = g.bfs(n1, n5)
        assert len(connected) == 5
        assert path == [n1, n2, n5]
        assert len(layers) == 3
    
    def test_dfs_search(self, g):
        res = g.dfs(3)
        print(res)
        assert len(res) == 5
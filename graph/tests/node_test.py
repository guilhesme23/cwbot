import pytest
from graph.node import Node

class TestNode:
    @pytest.fixture
    def n1(self):
        return Node(1)

    def test_idx_dont_change(self, n1):
        n1.idx = 2
        assert n1.idx == 1
    
    def test_enforce_integer_idx(self):
        with pytest.raises(TypeError):
            Node("not an index value")
    

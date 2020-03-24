class Node:
    """
    Base node class to be used with graph objects
    Any custom graph node must extend this class
    """
    def __init__(self, idx):
        if not isinstance(idx, int):
            raise TypeError
        self._idx = idx

    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self, _):
        self._idx = self._idx

    def __eq__(self, other):
        return self.idx == other.idx

    def __ne__(self, other):
        return self.idx != other.idx

    def __lt__(self, other):
        return self.idx < other.idx

    def __le__(self, other):
        return self.idx <= other.idx

    def __gt__(self, other):
        return self.idx > other.idx

    def __ge__(self, other):
        return self.idx >= other.idx

    def __hash__(self):
        return self.idx
    
    def __repr__(self):
        return f"<Node: {self.idx}>"

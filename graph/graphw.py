from collections import defaultdict
from functools import lru_cache

class GraphW:
    def __init__(self, g=None):
        if not g:
            self._g = defaultdict(list)
        else:
            self._g = g
        self.nodes = list(self._g.keys())
        self.weights = defaultdict(int)

    def __getitem__(self, item):
        return self._g[item]

    @lru_cache(maxsize=512)
    def get_by_idx(self, idx):
        try:
            return next(filter(lambda x: x.idx == idx, self.nodes))
        except StopIteration:
            return None
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, start, end, w=1):
        if isinstance(start, int) and isinstance(end, int):
            start = self.get_by_idx(start)
            end = self.get_by_idx(end)
        if end not in self._g[start]:
            self._g[start].append(end)
        self.weights[(start, end)] = w
    
    def add_bi_edge(self, start, end, w=1):
        if isinstance(start, int) and isinstance(end, int):
            start = self.get_by_idx(start)
            end = self.get_by_idx(end)
        if end not in self._g[start]:
            self._g[start].append(end)
        if start not in self._g[end]:
            self._g[end].append(start)

        self.weights[(start, end)] = w
        self.weights[(end, start)] = w
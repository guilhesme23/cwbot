from collections import defaultdict
from functools import lru_cache

class Graph:
    def __init__(self, g=None):
        if not g:
            self._g = {}
        else:
            self._g = g
        self.nodes = list(self._g.keys())

    def __getitem__(self, item):
        return self._g[item]

    @lru_cache(maxsize=256)
    def get_by_idx(self, idx):
        try:
            return next(filter(lambda x: x.idx == idx, self.nodes))
        except StopIteration:
            return None

    def add_node(self, n, edges):
        if not n or not isinstance(edges, list):
            return
        self._g[n] = set(edges)
        for node in edges:
            if node not in self._g:
                self._g[node] = set([])
            self._g[node].add(n)

        self.nodes.append(n)

    def bfs(self, key, target=None):
        """
        For each node, we check all it's neighbours
        before keep going to the next node
        """
        if isinstance(key, int):
            key = self.get_by_idx(key)
        if not key:
            raise IndexError

        components = [key]
        path_store = {}
        layers = [[key]]
        visited = defaultdict(lambda: False)
        for item in components:
            # This for only ends when there's no more
            # neighbours of a node that weren't visted yet
            visited[item] = True
            unvisited_neighbours = []
            for nbr in self._g[item]:
                if not visited[nbr]:
                    visited[nbr] = True
                    unvisited_neighbours.append(nbr)
                    path_store[nbr] = item
            if unvisited_neighbours:
                layers.append(unvisited_neighbours)
            # Append new nodes to the current connected set to keep iterating
            components.extend(unvisited_neighbours)

        if target:
            if isinstance(target, int):
                target = self.get_by_idx(target)

            path = self._gen_bfs_path(key, target, path_store)
            return components, layers, path
        else:
            return components, layers, None

    def _gen_bfs_path(self, s, t, paths):
        path = [t]

        for item in path:
            if paths[item] != s:
                path.append(paths[item])

        path.append(s)
        return path[::-1]

    def dfs(self, start):
        if isinstance(start, int):
            start = self.get_by_idx(start)
        
        visited = defaultdict(lambda: False)
        return list(self._dfs_iter(start, visited))
    
    def _dfs(self, node, visited):
        if not visited[node]:
            visited[node] = True
            yield node
            for nbr in self._g[node]:
                if not visited[nbr]:
                    yield from self._dfs(nbr, visited)
    
    def _dfs_iter(self, node, visited):
        stack = [node]
        while stack:
            curr = stack.pop()
            if not visited[curr]:
                visited[curr] = True
                yield curr
                stack.extend(self._g[curr])


    def show_graph(self):
        print('Nodes')
        [print(x) for x in list(self._g.keys())]
        print('Edges')
        for vals in self._g:
            print(self._g[vals])

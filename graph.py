class Graph:
  def __init__(self, g=None):
    if not g:
      self._g = {}
    else:
      self._g = g
    self.nodes = list(self._g.keys())

  def __getitem__(self, item):
    return self._g[item]

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
  
  def bfs(self, key):
    """
    For each node, we check all it's neighbours before keep going to the next node
    """
    if isinstance(key, int):
      key = self.get_by_idx(key)
    if not key:
      raise IndexError

    components = [key]
    for item in components:
      # This for only ends when there's no more neighbours of a node that weren't visted yet
      unvisited_neighbours = [x for x in self._g[item] if x not in components]
      components.extend(unvisited_neighbours) # Append new nodes to the current connected set to keep iterating

    return components

  def show_graph(self):
    print('Nodes')
    [print(x) for x in list(self._g.keys())]
    print('Edges')
    for vals in self._g:
      print(self._g[vals])

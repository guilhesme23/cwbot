from graph import Graph
from territory import Territory
from utils.build_graph import g

class WorldMap:
    def __init__(self, g: Graph):
        self._g = g
        self.territories = self._g.nodes
    
    def world_status(self):
        [print(x) for x in self.territories]

if __name__ == '__main__':
    map_ = WorldMap(g)
    map_.world_status()

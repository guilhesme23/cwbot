class Node:
    def __init__(self, idx):
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
    
    def __hash__(self):
        return self.idx

class Territory(Node):
    def __init__(self, idx, name, color="#FFFFFF"):
        super().__init__(idx)
        self.name = name
        self.dom = self
        self.color = color

    def __repr__(self):
      return f"<Territory: {self.idx}, {self.name}, dom: {self.dom.name}>"


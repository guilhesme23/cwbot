from graph.node import Node

class Territory(Node):
    def __init__(self, idx, name, color="#FFFFFF"):
        super().__init__(idx)
        self.name = name
        self.dom = self
        self.color = color

    def __repr__(self):
      return f"<Territory: {self.idx}, {self.name}, dom: {self.dom.name}>"


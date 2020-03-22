class Territory:
    def __init__(self, idx, name, color="#FFFFFF"):
        self.idx = idx
        self.name = name
        self.dom = self
        self.color = color

    def __repr__(self):
      return f"<Territory: {self.idx}, {self.name}, dom: {self.dom.name}>"
    
    def __eq__(self, other):
        return self.idx == other.idx
    
    def __ne__(self, other):
        return self.idx != other.idx

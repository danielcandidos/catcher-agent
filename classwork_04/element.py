
class ElementStatus:
    BLANK = 0
    WALL = 1
    AGENT = 2
    FOOD = 3
    OPEN = 4
    VISITED = 5
    CURRENT = 6

class Element:
    def __init__(self, i, j, status=ElementStatus.BLANK, generator=None, neighbors=[]):
        self.i = i
        self.j = j
        self.status = status
        self.generator = generator
        self.neighbors = neighbors
    
    @property
    def is_not_wall(self):
        return self.status != ElementStatus.WALL

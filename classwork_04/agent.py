from element import ElementStatus

class Agent:
    def __init__(self, start):
        self.visited = []
        self.opened = [start]
        self.element = start
        self.found = False
        self.stuck = False
        self.run = False

    def clean(self):
        self.visited = []
        self.opened = [self.element]
    
    def reset(self):
        self.clean()
        self.found = False
        self.stuck = False
        self.run = False

    def build_route(self):
        route = []
        element = self.element
        while True:
            route.append(element)
            if element.generator:
                element = element.generator
            else:
                break
        self.run = True
        return route
    
    def search(self):
        self.search_bfs()

    def search_bfs(self):
        if self.element.status == ElementStatus.FOOD:
            self.clean()
            self.found = True
        else:
            for neighbor in self.element.neighbors:
                if neighbor not in self.visited + self.opened:
                    neighbor.generator = self.element
                    self.opened.append(neighbor)
            self.visited.append(self.element)
            if self.opened:
                self.element = self.opened.pop(0)
            else:
                self.stuck = True

    def search_dfs(self):
        if self.element.status == ElementStatus.FOOD:
            self.clean()
            self.found = True
        else:
            for neighbor in self.element.neighbors:
                if neighbor not in self.visited + self.opened:
                    neighbor.generator = self.element
                    self.opened.append(neighbor)
            self.visited.append(self.element)
            if self.opened:
                self.element = self.opened.pop(0)
            else:
                self.stuck = True

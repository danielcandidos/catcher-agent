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
    
    def search(self, food=None):
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
                self.element = self.opened.pop(-1)
            else:
                self.stuck = True
    
    def search_ucs(self):
        if self.element.status == ElementStatus.FOOD:
            self.clean()
            self.found = True
        else:
            for neighbor in self.element.neighbors:
                if neighbor not in self.visited + self.opened:
                    neighbor.generator = self.element
                    neighbor.g = self.element.g + 1
                    self.opened.append(neighbor)
            self.visited.append(self.element)
            if self.opened:
                self.opened.sort(key=lambda element: element.g)
                self.element = self.opened.pop(0)
            else:
                self.stuck = True

    def search_greedy(self, food):
        if self.element.status == ElementStatus.FOOD:
            self.clean()
            self.found = True
        else:
            for neighbor in self.element.neighbors:
                if neighbor not in self.visited + self.opened:
                    neighbor.generator = self.element
                    neighbor.calculate_manhattan_distance(food)
                    self.opened.append(neighbor)
            self.visited.append(self.element)
            if self.opened:
                self.opened.sort(key=lambda element: element.d)
                self.element = self.opened.pop(0)
            else:
                self.stuck = True

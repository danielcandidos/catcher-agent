import random
from element import Element, ElementStatus

class Matrix:
    def __init__(self, height=600, width=600, cells_num=20):
        self.height = height
        self.width = width
        self.cells_num = cells_num
        self.elements = []
        self.agent = None
        self.food = None

    def initialize(self):
        self.build_matrix()
        self.add_agent()
        self.add_food()
        self.add_walls()
        self.add_neighbors()

    def build_matrix(self):
        for i in range(self.cells_num):
            row = [Element(i, j) for j in range(self.cells_num)]
            self.elements.append(row)
    
    def add_agent(self):
        i, j = self.search_blank()
        self.elements[i][j].status = ElementStatus.AGENT
        self.agent = self.elements[i][j]
    
    def add_food(self):
        i, j = self.search_blank()
        self.elements[i][j].status = ElementStatus.FOOD
        self.food = self.elements[i][j]

    def add_walls(self):
        num_walls = self.cells_num * 3
        for _ in range(num_walls):
            i, j = self.search_blank()
            self.elements[i][j].status = ElementStatus.WALL
    
    def add_neighbors(self):
        for i in range(self.cells_num):
            for j in range(self.cells_num):
                neighbors = []
                up, right, down, left = i-1, j+1, i+1, j-1
                if up >= 0 and self.elements[up][j].is_not_wall:
                    neighbors.append(self.elements[up][j])
                if right < self.cells_num and self.elements[i][right].is_not_wall:
                    neighbors.append(self.elements[i][right])
                if down < self.cells_num and self.elements[down][j].is_not_wall:
                    neighbors.append(self.elements[down][j])
                if left >= 0 and self.elements[i][left].is_not_wall:
                    neighbors.append(self.elements[i][left])
                self.elements[i][j].neighbors = neighbors
    
    def update(self, visited, opened, current):
        self.clean()
        for element in visited:
            if element not in [self.agent, self.food]:
                self.elements[element.i][element.j].status = ElementStatus.VISITED
        for element in opened:
            if element not in [self.agent, self.food]:
                self.elements[element.i][element.j].status = ElementStatus.OPEN
        if current not in [self.agent, self.food]:
            self.elements[current.i][current.j].status = ElementStatus.CURRENT
    
    def move_agent(self, element):
        self.clean()
        self.agent.status = ElementStatus.BLANK
        self.elements[element.i][element.j].status = ElementStatus.AGENT
        self.agent = element
    
    def clean(self):
        for row in self.elements:
            for element in row:
                fixed = [ElementStatus.AGENT, ElementStatus.FOOD, ElementStatus.WALL]
                if element.status not in fixed:
                    element.status = ElementStatus.BLANK

    def search_blank(self):
        while True:
            i = random.randint(0, self.cells_num - 1)
            j = random.randint(0, self.cells_num - 1)
            if self.elements[i][j].status == ElementStatus.BLANK:
                return i, j
    
    def display(self):
        element_height = int(self.height / self.cells_num)
        element_width = int(self.width / self.cells_num)
        center_y = 12
        for row in self.elements:
            center_x = 12
            for element in row:
                if element.status == ElementStatus.BLANK:
                    stroke(255, 255, 255)
                    fill(255, 255, 255)
                elif element.status == ElementStatus.WALL:
                    stroke(0, 0, 0)
                    fill(0, 0, 0)
                elif element.status == ElementStatus.AGENT:
                    stroke(0, 0, 128)
                    fill(0, 0, 128)
                elif element.status == ElementStatus.FOOD:
                    stroke(255, 0, 0)
                    fill(255, 0, 0)
                elif element.status == ElementStatus.OPEN:
                    stroke(255, 215, 0)
                    fill(255, 215, 0)
                elif element.status == ElementStatus.VISITED:
                    stroke(255, 140, 0)
                    fill(255, 140, 0)
                elif element.status == ElementStatus.CURRENT:
                    stroke(65, 105, 225)
                    fill(65, 105, 225)
                ellipse(center_x, center_y, element_width-6, element_height-6)
                center_x += element_width
            center_y += element_height

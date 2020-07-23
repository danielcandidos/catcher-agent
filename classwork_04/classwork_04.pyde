from agent import Agent
from matrix import Matrix

def setup():
    global matrix, agent, route

    matrix = Matrix()
    matrix.initialize()

    agent = Agent(matrix.agent)

    size(600, 600)
    background(255, 255, 255)

def draw():
    global matrix, agent, route

    frameRate(20)
    matrix.display()

    if agent.found:
        if not agent.run:
            route = agent.build_route()
        elif route:
            element = route.pop()
            matrix.move_agent(element)
            matrix.display()
        else:
            agent.reset()
            matrix.add_food()
    else:
        agent.search()
        matrix.update(agent.visited, agent.opened, agent.element)

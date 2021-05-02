from config import *

class fixedObstacle:
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def setTree(self, x, y):
        self.x = x
        self.y = y
        window.blit(tree, (self.x, self.y))

    def setRock(self, x, y):
        self.x = x
        self.y = y
        window.blit(rock, (self.x, self.y))

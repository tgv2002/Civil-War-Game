from config import *
class movingObstacle:
    
    def __init__(self):
        self.x = 0
        self.y = 80

    def setShip(self, x, y):
        self.x = x
        self.y = y
        window.blit(ship, (self.x, self.y))
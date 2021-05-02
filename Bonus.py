from config import *

class Bonus:
    
    def __init__(self):
        self.x = 0
        self.y = 90

    def setShield(
        self,
        x,
        y,
        vis_shield,
    ):
        self.x = x
        self.y = y
        if vis_shield:
            window.blit(shield, (self.x, self.y))

    def setHeart(
        self,
        x,
        y,
        vis_heart,
    ):
        self.x = x
        self.y = y
        if vis_heart:
            window.blit(heart, (self.x, self.y))
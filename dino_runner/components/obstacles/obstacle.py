from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
class Obstacle:
    def __init__ (self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
class Cactus(Obstacle):
    def __init__(self, pos_x, pos_y, type):
        super().__init__()
        self.type = type
        if self.type == "small":
           self.image = SMALL_CACTUS
        elif self.type == "large":
           self.image = LARGE_CACTUS
        pass



        
        




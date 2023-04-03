from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, SCREEN_HEIGHT, SCREEN_WIDTH, CLOUD
import pygame
import random
game_speed = 20
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
class Cloud(Obstacle):
    def __init__(self):
        super().__init__()
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image_cloud = CLOUD
        self.width = self.image_cloud.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image_cloud, (self.x, self.y))


   
            
    
















    
        
        




        
    
        

        

        
            
            

            
            



        





        
        




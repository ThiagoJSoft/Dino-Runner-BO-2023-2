from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game_speed, player):
        select_obstacle = random.randint(0, 1)
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus()) if select_obstacle == 0 else self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed, player)
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
        

    

    
        
        


    

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    




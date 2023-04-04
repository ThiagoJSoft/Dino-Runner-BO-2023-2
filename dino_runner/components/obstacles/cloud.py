import random
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
game_speed = 20
class Cloud:
    def __init__(self):   
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image_cloud = CLOUD
        self.width = self.image_cloud.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(500, 1000)
            self.y = random.randint(50, 100)
    def draw(self, SCREEN):
        SCREEN.blit(self.image_cloud, (self.x, self.y))
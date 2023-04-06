from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.power_ups.append(Shield())
        self.power_ups.append(Hammer())

    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % 200 == 0:
            self.generate_power_up(game_speed, player)
        
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)
            

    def generate_power_up(self, game_speed, player):
        x = random.randint(SCREEN_WIDTH + 200, SCREEN_WIDTH + 400)
        y = PowerUp.Y_POS_POWER_UP
        random_power_up = random.choice([Shield(), Hammer()])
        random_power_up.rect.x = x
        random_power_up.rect.y = y
        self.power_ups.append(random_power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
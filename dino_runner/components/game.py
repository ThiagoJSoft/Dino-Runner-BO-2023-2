import pygame
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SOL, ruta_musica
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager  
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.play(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
        

        

        

        


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.cloud.update()
            self.player.update(user_input)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.points += 1
            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1
            

        
        

        
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            if self.player.hammering:
                self.player.draw_hammer(self.screen)
            self.player.draw(self.screen)
            self.cloud.draw(self.screen)
            self.obstacle_manager.draw(self.screen, self.player)
            self.power_up_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        

        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(SOL,(0, 0))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed 
        
        

    def draw_score(self):
        score, score_rect = text_utils.get_message('Points: ' + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)


    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()

    def print_menu_element(self):
        if self.death_count == 0:

            text, text_rect = text_utils.get_message('Press any Key to Start', 30)
            self.screen.blit(text, text_rect)

        else:
            text, text_rect = text_utils.get_message('Press any Key to Restart', 30)
            score, score_rect = text_utils.get_message('Your score: '+ str(self.points), 30, height=SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)

    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0

    


    
    
        

    
        

    
            



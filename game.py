import pygame
from .scripts.player import Player

pygame.init()


pygame.display.set_caption('platformer game')
class Game:
    def __init__(self,size):
        self.screen = pygame.display.set_mode((size))
        self.running=True
        self.assets={
            'player'
        }
        self.clock=pygame.time.Clock()
        self.player=Player()
    def run(self):
       while self.running:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running=False
            
            pygame.display.update()
            self.clock.tick(60)

Game((1000,800),).run()
            
             
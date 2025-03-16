import pygame
from scripts.player import Player
from scripts.util import load_image
pygame.init()


pygame.display.set_caption('platformer game')
class Game:
    def __init__(self,size):
        self.size=list(size)
        self.screen = pygame.display.set_mode((size))
        self.display=pygame.Surface((self.size[0]//2,self.size[1]//2))
        self.running=True
        self.assets={
            'player':load_image('entities/player/idle/00.png')
        }
        self.clock=pygame.time.Clock()
        self.player=Player(self,self.assets['player'],(200,200))

    def run(self):
       while self.running:
            # 
            self.display.fill((20,120,230))
            
            self.player.render(self.display)

            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running=False
            
            self.screen.blit(pygame.transform.scale2x(self.display),(0,0))            
            pygame.display.update()
            self.clock.tick(60)

Game((1200,800),).run()
            
             
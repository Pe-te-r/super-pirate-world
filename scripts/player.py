import pygame
from .physics import PhysicsEntity

class Player(PhysicsEntity):
    def __init__(self, game, image, positon):
        super().__init__(game, image, positon)
        self.move_speed=0.5
        self.acceleration=pygame.Vector2(0,self.gravity)
    
    def key_press(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acceleration.x -= self.move_speed
        if keys[pygame.K_d]:
            self.acceleration.x += self.move_speed
        
        if keys[pygame.K_w]:
            self.velocity.y =self.jump_force
        
        
        
    def update(self):
        self.key_press()
        
        self.acceleration.x += self.velocity.x * -self.drag
        
        self.velocity += self.acceleration
        self.position += self.velocity+0.5*self.acceleration
        self.frect.topleft=self.position
from pygame.math import  Vector2
class PhysicsEntity:
    def __init__(self,game,image,positon):
        self.game=game
        self.image=image
        self.position=Vector2(positon)
        self.frect=self.image.get_frect(topleft=self.position)
        self.friction=0.1
        self.jump_force=-12
        self.max_speed=5    
        self.gravity=0.5
        self.drag=0.9
        self.velocity=Vector2(0,0)
    def update(self):
        pass
    
    def render(self,surf):
        surf.blit(self.image,self.frect)
class PhysicsEntity:
    def __init__(self,game,image,positon):
        self.game=game
        self.image=image
        self.frect=self.image.get_frect(topleft=self.position)
        self.position=positon
    def update(self):
        pass
    
    def render(self,surf):
        surf.blit(self.image,self.frect)
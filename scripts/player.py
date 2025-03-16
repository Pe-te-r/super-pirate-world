from .physics import PhysicsEntity

class Player(PhysicsEntity):
    def __init__(self, game, image, positon):
        super().__init__(game, image, positon)
        
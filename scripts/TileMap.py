from pygame import Vector2
class Tile:
    def __init__(self,position,img,tile_size=16):
        self.position=position
        self.img=img
        self.frect=self.img.get_frect(topleft=Vector2(self.position))
        self.tile_size=tile_size
    
    def render(self,surf):
        surf.blit(self.img,self.frect)


class TileMap:
    def __init__(self):
        self.tiles_map={}
    
    def add_tiles(self):
        pass
    
    def render(self,surf):
        pass
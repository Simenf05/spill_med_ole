import pygame as pg
import map
import math


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800


for i in map.maps:
    print(i)

pg.init()

class Player:
    
    def __init__(self, coords: tuple):
        
        
        self.box = pg.Rect(coords[0], coords[1], 40, 40)
        self.color = pg.Color("Purple")
        
    def movement(self, keys):
        
        if keys[pg.K_SPACE]:
            
            self.box.move_ip(0, -10)
            

class Block:
    def __init__(self):
        pass
        


class GameLoop:
    
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        
        self.player = Player((100, 100))
        
        self.blocks = []
        
        for i, block in enumerate(map.maps):
            self.blocks.append(pg.Rect(
                
                (i) * (math.floor(SCREEN_WIDTH / len(map.maps))),
                SCREEN_HEIGHT - (math.floor(SCREEN_HEIGHT / len(block))),
                
                
                (SCREEN_WIDTH / len(map.maps)), 
                (SCREEN_HEIGHT / len(block))
                ))
        
        
        self.alive = True
        
        
        
        
    def run(self):
        
        while self.alive:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.alive = False
            keys = pg.key.get_pressed()
            self.screen.fill("black")
            
            
            
            
            
            for draw in self.blocks:
                pg.draw.rect(self.screen, "red", draw)
            
            pg.draw.rect(self.screen, self.player.color, self.player.box)
            
            
        
            self.player.movement(keys)
            
            
            pg.display.update()
            self.clock.tick(60)
                    
    
            
            

        
if __name__ == "__main__":
    game = GameLoop()
    game.run()
    
    
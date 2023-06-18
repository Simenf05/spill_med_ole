from calendar import c
import pygame as pg
import map
import math


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

pg.init()

class Player:
    
    def __init__(self, coords: tuple):
        
        
        self.box = pg.Rect(coords[0], coords[1], 40, 40)
        self.color = pg.Color("Purple")
        self.verticalSpeed = 0
        
        self.onGround = False
    
    def updateGrav(self):
        if self.onGround:
            self.verticalSpeed = 0
            
        else:
            self.verticalSpeed -= .2
    
    def press(self, keys):
        if keys[pg.K_SPACE] and self.onGround:
            
            self.onGround = False
            self.verticalSpeed += 1
            
    def onGroundCheck(self, list) -> bool:
        
        check = self.box.collidelist(list)
        
        if check == -1:
            return False
        
        return check
        
        
    def movement(self, move: tuple):
        self.box.move_ip(move)
        



class GameLoop:
    
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.alive = True
        
        self.player = Player((100, 100))
        
        self.blocks = []
        self.blockSize = 40
        self.blocksOnScreen = 35
        
        
        for i, row in enumerate(map.maps):
            
            for j, block in enumerate(row):
                
                if block == "b":
                    
                    self.blocks.append(pg.Rect(
                        
                        (i) * (math.floor(SCREEN_WIDTH / self.blocksOnScreen)),
                        SCREEN_HEIGHT - (math.floor((j + 1) * (SCREEN_HEIGHT / len(row)))),
                        SCREEN_WIDTH / self.blocksOnScreen,
                        SCREEN_HEIGHT / len(row)
                        ))
        
        
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
            
            
            self.player.onGround = self.player.onGroundCheck(self.blocks)
            
            self.player.press(keys)
            
            self.player.updateGrav()
            
            self.player.movement((0, -self.player.verticalSpeed))
            
            pg.display.update()
            self.clock.tick(60)
                    
    
            
            

        
if __name__ == "__main__":
    game = GameLoop()
    game.run()
    

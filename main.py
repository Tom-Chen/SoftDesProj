import os
import sys
import pygame
from pygame.locals import *
import Tank
import Projectile

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

global RED
RED = (255,0,0)
global BLUE
BLUE = (0,0,255)
global SKY
SKY = (105,140,255)
global GROUND
GROUND = (209,155,96)
global GRAVITY
GRAVITY = 1
global TURN
TURN = 0
global FPS
FPS = 60

class TankMain():
  #Initializes game
  def __init__(self, width=800,height=600):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.screen.fill(SKY, rect=None, special_flags=0)
    self.background = pygame.Surface((self.width,self.height))
    self.background.fill(SKY ,rect=None, special_flags=0)
    pygame.display.set_caption('Tank!')
    self.LoadSprites()
    self.side = 1
  
  def MainLoop(self):
  #Primary loop/event queue
    current = pygame.time.get_ticks()
    while 1:      
      if(pygame.time.get_ticks()-current>FPS/10):
        for event in pygame.event.get():
          if event.type == pygame.QUIT: 
            sys.exit()
          elif event.type == KEYDOWN:
            if ((event.key == K_RIGHT) or (event.key == K_LEFT)):
              if (self.side == 0):
                self.bluetank.move(event.key)
              elif (self.side == 1):
                self.redtank.move(event.key)
            if(event.key == K_SPACE):
              #switch sides, eventually control firing
              if (self.side == 0):
                self.side = 1
                bluetankpos = self.bluetank.rect.center
                self.reloadProjectiles(bluetankpos[0], bluetankpos[1],4,-6)
              elif (self.side == 1):
                self.side = 0
                redtankpos = self.redtank.rect.center
                self.reloadProjectiles(redtankpos[0], redtankpos[1],-4,-6)
        self.redtank_sprite.clear(self.screen,self.background)
        self.bluetank_sprite.clear(self.screen,self.background)
        self.projectile_sprites.clear(self.screen,self.background)
        self.redtank_sprite.draw(self.screen)
        self.bluetank_sprite.draw(self.screen)
        self.projectile.domove()
        self.projectile_sprites.draw(self.screen)
        pygame.display.flip()
        current = pygame.time.get_ticks()
    
  def LoadSprites(self):
  #Handles sprites
    self.bluetank = Tank.Tank(side=0)
    self.redtank = Tank.Tank(side=1)
    self.bluetank_sprite = pygame.sprite.RenderPlain((self.bluetank))
    self.redtank_sprite = pygame.sprite.RenderPlain((self.redtank))
    self.projectile = Projectile.Projectile(100, 100, 4, -6, pygame.time.get_ticks())
    self.projectile_sprites = pygame.sprite.RenderPlain((self.projectile))
  
  def reloadProjectiles(self,x,y,xv,yv):
    self.projectile = Projectile.Projectile(x,y,xv,yv, pygame.time.get_ticks())
    self.projectile_sprites = pygame.sprite.RenderPlain((self.projectile))

#Starts game if run from command line
if __name__ == "__main__":
  MainWindow = TankMain()
  MainWindow.MainLoop()

import os
import sys
import pygame
from pygame.locals import *
import Tank
import Projectile

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

global RED
RED = (255,0,0)
global BLUE
BLUE = (0,0,255)
global SKY
SKY = (105,140,255)
global GROUND
GROUND = (209,155,96)
global GRAVITY
GRAVITY = -5


class TankMain():
  #Initializes game
  def __init__(self, width=800,height=600):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.screen.fill(SKY, rect=None, special_flags=0)
    pygame.display.set_caption('Tank!')
    ground = pygame.Rect(0,540,width,60)
    mountain = pygame.Rect(300,300,200,500)
    self.screen.fill(GROUND, rect=ground, special_flags=0)
    self.screen.fill(GROUND, rect=mountain, special_flags=0)
    self.tank = Tank()
        
  def MainLoop(self):
    #Primary loop/event queue
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()
      self.projectile.domove()
      self.tank_sprites.draw(self.screen)
      self.projectile_sprites.draw(self.screen)
      pygame.display.flip()
	  self.screen.blit(self.tank,(pygame.mouse.get_pos()[0],100))
      
  def LoadSprites(self):
    #Handles sprites
    self.tank = Tank.Tank()
    self.projectile = Projectile.Projectile(0, 1, pygame.time.get_ticks())
    self.tank_sprites = pygame.sprite.RenderPlain((self.tank))
    self.projectile_sprites = pygame.sprite.RenderPlain((self.projectile))

#Starts game if run from command line
if __name__ == "__main__":
  MainWindow = TankMain()
  MainWindow.MainLoop()

import os
import sys
import pygame
import main
from pygame.locals import *
import math

class Projectile(pygame.sprite.Sprite):
  def __init__(self,x,y, angle, power, timezero, color):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('./img/shot.png')
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)
    self.angle = math.radians(angle)
    self.xv = int(math.cos(self.angle)*power)
    self.yv = int(math.sin(self.angle)*power)

    self.timezero = timezero
    self.color = color
  def domove(self):
    dx = self.xv
    dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)/main.FPS
    self.rect.move_ip(dx, dy)
    self.rect.move(dx, dy)

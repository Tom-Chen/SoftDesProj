import os
import sys
import pygame
from pygame.locals import *
import main


class Tank(pygame.sprite.Sprite):
  #Defines a tank
  def __init__(self,side):
    pygame.sprite.Sprite.__init__(self) 
    if(side == 0):
      self.image = pygame.image.load('bluetank.png')
      self.rect = (100,100,550,50)
    if(side == 1):
      self.image = pygame.image.load('redtank.png')
      self.rect = (500,100,550,50)
    self.health = 1000
    self.angle = 90
    self.power = 100
    self.color = None

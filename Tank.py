import os
import sys
import pygame
from pygame.locals import *
import main


class Tank(pygame.sprite.Sprite):
  #Defines a tank
  def __init__(self,left=103,top=97):
    pygame.sprite.Sprite.__init__(self) 
    self.image, self.rect = main.load_image('tank.png',-1)
    self.rect.left = left
    self.rect.top = top
    self.health = 1000
    self.angle = 90
    self.power = 100
    self.color = None

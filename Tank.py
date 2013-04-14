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
      self.rect = pygame.Rect(100,100,550,50)
      self.color = "blue"
    if(side == 1):
      self.image = pygame.image.load('redtank.png')
      self.rect = pygame.Rect(500,100,550,50)
      self.color = "red"
    self.health = 1000
    self.angle = 90
    self.power = 100
    self.x_dist = 5
    self.y_dist = 5
    
  def move(self,key):
    xMove = 0;
    yMove = 0;
    
    if (key == K_RIGHT):
        xMove = self.x_dist
        print("Right")
    elif (key == K_LEFT):
        xMove = -self.x_dist
        print("Left")
    elif (key == K_UP):
        yMove = -self.y_dist
        print("Up")
    elif (key == K_DOWN):
        yMove = self.y_dist
        print("Down")
    self.rect.move_ip(xMove,yMove);

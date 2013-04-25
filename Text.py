import os
import sys
import pygame
from pygame.locals import *
import main

#Defines easily erasable text objects
class Text(pygame.sprite.Sprite):

  def __init__(self, text, font, color, topleft):
      pygame.sprite.Sprite.__init__(self)
      self.image = font.render(str(text), True, color)
      self.rect = self.image.get_rect()
      self.rect.topleft = topleft
      self.font = font
      self.color = color

  def refresh(self, text):
      oldCenter = self.rect.center
      self.image = self.font.render(str(text), True, self.color)
      self.rect = self.image.get_rect()
      self.rect.center = oldCenter
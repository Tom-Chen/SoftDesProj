import os
import sys
import pygame
import main
from pygame.locals import *
import math

class Terrain(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/cliff.png')
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)


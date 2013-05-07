import os
import sys
import pygame
import main
from pygame.locals import *
import math

class Terrain(pygame.sprite.Sprite):
	def __init__(self,x,y,imgName):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/' + imgName + '.png')
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
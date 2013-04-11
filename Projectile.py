import os
import sys
import pygame
import main
from pygame.locals import *

class Projectile(pygame.sprite.Sprite):
	def __init__(self, xv, yv, timezero):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = main.load_image('tank.png',-1)
		self.xv = xv
		self.yv = yv
	def move(self):
		self.rect.center[0] += self.xv
		self.rect.center[1] += self.yv + main.GRAVITY*(TIME-self.timezero)

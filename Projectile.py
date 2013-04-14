import os
import sys
import pygame
import main
from pygame.locals import *

class Projectile(pygame.sprite.Sprite):
	def __init__(self, xv, yv, timezero):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('shot.png')
		self.rect = self.image.get_rect()
		self.xv = int(xv)
		self.yv = int(yv)
		self.timezero = timezero
	def domove(self):
		dx = self.xv
		dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)
		self.rect.move(dx, dy)
import os
import sys
import pygame
import main
from pygame.locals import *

class Projectile(pygame.sprite.Sprite):
	def __init__(self, xv, yv, timezero):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('shot.png')
		#self.rect = self.image.get_rect()
		self.rect = pygame.Rect(100,100,550,50)
		self.xv = int(xv)
		self.yv = int(yv)
		self.timezero = timezero
	def domove(self):
		dx = self.xv
		dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)/1000
		self.rect.move_ip(dx, dy)

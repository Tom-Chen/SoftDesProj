import os
import sys
import pygame
import main
from pygame.locals import *

class Projectile(pygame.sprite.Sprite):
	def __init__(self,x,y, xv, yv, timezero):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('shot.png')
		self.rect = self.image.get_rect()
<<<<<<< HEAD
=======
		self.rect.center = (x,y)
>>>>>>> 81a56cc7c6f62a9a96b68519a392b0261f1d8184
		self.xv = int(xv)
		self.yv = int(yv)
		self.timezero = timezero
	def domove(self):
		dx = self.xv
<<<<<<< HEAD
		dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)
		self.rect.move(dx, dy)
=======
		dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)/1000
		self.rect.move_ip(dx, dy)
>>>>>>> 81a56cc7c6f62a9a96b68519a392b0261f1d8184

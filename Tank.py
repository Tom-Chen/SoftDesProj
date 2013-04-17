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
			self.rect = self.image.get_rect()
			self.rect.center = (100,100)
			self.color = "blue"
			self.angle = 0
		if(side == 1):
			self.image = pygame.image.load('redtank.png')
			self.rect = self.image.get_rect()
			self.rect.center = (500,100)
			self.color = "red"
			self.angle = 180
		self.health = 1000
		self.angle = 90
		self.power = 100
		self.x_dist = 5
		
	def move(self,key):
		xMove = 0;
		if (key == K_UP):
			self.angle += 15
		elif (key == K_DOWN):
			self.angle -= 15
		elif (key == K_RIGHT):
			xMove = self.x_dist
			print("Right")
		elif (key == K_LEFT):
			xMove = -self.x_dist
			print("Left")
			
#		if self.angle >360:
#			self.angle -=360
#		if self.angle <=0:
#			self.angle +=360
		print(self.color,self.angle)
		if self.color == 'red':
			if self.angle <= 180:
				self.angle = 180
			if self.angle >= 270:
				self.angle = 270
		if self.color == 'blue':
			if self.angle <= 270:
				self.angle = 270
			if self.angle >= 360:
				self.angle = 360
		self.rect.move_ip(xMove,0)
		self.rect.move(xMove,0)

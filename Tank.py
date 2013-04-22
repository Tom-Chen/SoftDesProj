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
			self.image = pygame.image.load('./img/bluetank315.png')
			coords = self.image.get_rect()
			self.rect = pygame.Rect(coords[0], coords[1]+40, coords[2], coords[3]-40)
			self.rect.center = (100,100)
			self.color = "blue"
			self.angle = 315
		if(side == 1):
			self.image = pygame.image.load('./img/redtank225.png')
			coords = self.image.get_rect()
			self.rect = pygame.Rect(coords[0], coords[1]+40, coords[2], coords[3]-40)
			self.rect.center = (500,100)
			self.color = "red"
			self.angle = 225

		print(self.rect)

		self.health = 1000
		self.power = 10
		self.x_dist = 5
		
	def move(self,key):
		xMove = 0;
		if (key == K_UP):
			if self.color == 'blue':
				self.angle -=15
			else:
				self.angle += 15
		elif (key == K_DOWN):
			if self.color == 'blue':
				self.angle +=15
			else:
				self.angle -= 15
		elif (key == K_RIGHT):
			xMove = self.x_dist
			print("Right")
		elif (key == K_LEFT):
			xMove = -self.x_dist
			print("Left")
		if key == K_p:
			self.power += 1
			if self.power>main.MAXSPEED:
				self.power == 0
			print("power", self.power)
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
		newImage = './img/'+self.color+'tank'+str(self.angle)+'.png'
		self.image = pygame.image.load(newImage)
		self.rect.move_ip(xMove,0)
		self.rect.move(xMove,0)

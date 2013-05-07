import os
import sys
import pygame
from pygame.locals import *
import main

class Tank(pygame.sprite.Sprite):
	#Defines a tank
	def __init__(self,side):
		pygame.sprite.Sprite.__init__(self)
				#Differentiate red/blue tanks
		if(side == 0):
			self.image = pygame.image.load('./img/bluetank315.png')
			coords = self.image.get_rect()
			self.rect = pygame.Rect(coords[0], coords[1], coords[2], coords[3])
			self.rect.center = (main.WIDTH/4,main.HEIGHT- main.HEIGHT/4)
			self.color = "blue"
			self.angle = 315
			self.ai = False
		if(side == 1):
			self.image = pygame.image.load('./img/redtank225.png')
			coords = self.image.get_rect()
			self.rect = pygame.Rect(coords[0], coords[1], coords[2], coords[3])
			self.rect.center = (main.WIDTH - main.WIDTH/4,main.HEIGHT- main.HEIGHT/4)
			self.color = "red"
			self.angle = 225
			self.ai = False
		#Common parameters
		self.moveBack = False
		self.adjustshot = 0
		self.fireMode = 0
		self.health = 500
		self.power = 50
		self.x_dist = 3
		self.weapon= "Standard"
		
	def adjust(self,key):

		xMove = 0;
		#Angle Adjustment
		self.angle = adjustAngle(self.color,self.angle,key)
		#Movement
		if (key == K_RIGHT):
			xMove = self.x_dist
		elif (key == K_LEFT):
			xMove = -self.x_dist
		#Change power
		if key == K_p:
			self.power += 1
			if self.power>main.MAXSPEED:
				self.power = 1
		#Cap the Angle
		self.angle = capAngle(self.color,self.angle)
		#Adjust image based on angle
		approxAngle = round(self.angle / 15) * 15
		newImage = './img/'+self.color+'tank'+str(int(approxAngle))+'.png'
		self.image = pygame.image.load(newImage)
		#Actually move
		self.rect.move_ip(xMove,0)
		self.rect.move(xMove,0)
		
def capAngle(color, angle):
	#Caps the angle of the gun based on which tank it is
	if color == 'red':
		if angle <= 180:
			return 180
		if angle >= 270:
			return 270
	if color == 'blue':
		if angle <= 270:
			return		270
		if angle >= 360:
			return 360
	return angle

def adjustAngle(color, angle, key):
	#Adjusts the angle of the tank's gun
	if (key == K_UP):
		if color == 'blue':
			return (angle - 1)
		else:
			return (angle + 1)
	if (key == K_DOWN):
		if color == 'blue':
			return (angle + 1)
		else:
			return (angle - 1)
	return angle

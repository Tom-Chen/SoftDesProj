import os
import sys
import pygame
import main
from pygame.locals import *
import math

class Projectile(pygame.sprite.Sprite):
	def __init__(self,x,y, angle, power, timezero, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/shot.png')
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.angle = math.radians(angle)
		self.xv = int(math.cos(self.angle)*power)
		self.yv = int(math.sin(self.angle)*power)
		self.dx = 0
		self.dy = 0
		self.doTrack = False
		self.timezero = timezero
		self.color = color
		self.power = power
		self.damage = 50
	def domove(self):
		if self.doTrack:
			values = self.track()
			self.dx += values[0]
			self.dy += values[1]
			if self.dx >= 6:
				self.dx = 6
			if self.dy >= 6:
				self.dy = 6
		else:
			self.dx = self.xv
			self.dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)/main.FPS
		
		self.rect.move_ip(self.dx, self.dy)
		self.rect.move(self.dx, self.dy)
	def setTarget(self,x, y):
		self.targetx = x
		self.targety = y
		self.doTrack = True
	def split(self):#NOTE: out of commision until multiple projectile support is added.
		returnlist = []
		for i in range(-30,30,15):
			returnlist.append([self.rect.center[0],self.rect.center[1], math.degrees(math.atan2(self.dy,self.dx))+i,math.sqrt(self.dy*self.dy+self.dx*self.dx),pygame.time.get_ticks(), self.color])
		return returnlist
	
	def track(self):
		xdif = self.rect.center[0] - self.targetx
		ydif = self.rect.center[1] - self.targety
		difangle = math.atan2(ydif,xdif)

		dx = -(math.cos(difangle)*.5)
		dy = -(math.sin(difangle)*.5)
		return [dx,dy]

import pygame
import main
from pygame.locals import *
import math

class Projectile(pygame.sprite.Sprite):
	def __init__(self,x,y, angle, power, timezero, color, mode, target):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/shot.png')
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.angle = math.radians(angle)
		self.xv = int(math.cos(self.angle)*power)
		self.yv = int(math.sin(self.angle)*power)
		self.dx = self.xv
		self.dy = self.yv
		self.doTrack = False
		self.timezero = timezero
		self.color = color
		self.power = power
		self.damage = 50
		self.hitScan = False
		self.queueSplit = False
		self.projectiles = []
		self.splitMain = False
		self.drop = False
		self.queueDrop = False
		if mode == 4:
			self.hitScanEnable()
		if mode == 2:
			self.setTarget(target[0],target[1])
		if mode == 3:
			self.queueSplit = True
		if mode == 5:
			self.queueDrop = True
			
	def domove(self):
		if self.doTrack and checkTime(self.timezero):
			values = self.track()
			self.dx += values[0]
			self.dy += values[1]
			if self.dx >= 6:
				self.dx = 6
			if self.dy >= 6:
				self.dy = 6
		elif self.hitScan:
			self.dx = self.dx
			self.dy = self.dy
		else:
			self.dx = self.xv
			self.dy = self.yv + main.GRAVITY*(pygame.time.get_ticks()-self.timezero)/main.FPS
			if self.queueSplit:
				if checkTime(self.timezero):
					self.splitMain = True
			if self.queueDrop:
				if checkTime(self.timezero):
					self.drop = True
					self.damage *=2
					self.queueDrop = False
			if self.drop:
				self.dx = 0
		
		self.rect.move_ip(self.dx, self.dy)
		self.rect.move(self.dx, self.dy)
	def setTarget(self,x, y):
		self.damage/=2
		self.targetx = x
		self.targety = y
		self.doTrack = True
		self.hitScan = False
	def split(self):
		returnlist = []
		for i in range(-30,30,15):
			returnlist.append([self.rect.center[0],self.rect.center[1], math.degrees(math.atan2(self.dy,self.dx))+i,math.sqrt(self.dy*self.dy+self.dx*self.dx),pygame.time.get_ticks(), self.color,0,(0,0)])
		return returnlist
	def hitScanEnable(self):
		self.hitScan = True
		self.doTrack = False
	
	def track(self):
		xdif = self.rect.center[0] - self.targetx
		ydif = self.rect.center[1] - self.targety
		difangle = math.atan2(ydif,xdif)

		dx = -(math.cos(difangle)*.5)
		dy = -(math.sin(difangle)*.5)
		return [dx,dy]
		
def checkTime(timezero):
	if pygame.time.get_ticks()-timezero >= 1000:
		return True
	return False

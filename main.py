import os
import sys
import pygame
from pygame.locals import *
import Tank
import Projectile

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

global RED
RED = (255,0,0)
global BLUE
BLUE = (0,0,255)
global SKY
SKY = (105,140,255)
global GROUND
GROUND = (209,155,96)
global GRAVITY
GRAVITY = 1
global TURN
TURN = 0
global FPS
FPS = 60
global MAXSPEED
MAXSPEED = 20

class TankMain():
	#Initializes game
	def __init__(self, width=800,height=600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(SKY, rect=None, special_flags=0)
		self.background = pygame.Surface((self.width,self.height))
		self.background.fill(SKY ,rect=None, special_flags=0)
		pygame.display.set_caption('Tank!')
		self.LoadSprites()
		self.side = 1
	
	def MainLoop(self):
	#Primary loop/event queue
		current = pygame.time.get_ticks()
		while 1:
			#FPS and gamespeed limiter
			if(pygame.time.get_ticks()-current>(1000/FPS)):
				for event in pygame.event.get():
					if event.type == pygame.QUIT: 
						sys.exit()
					elif event.type == KEYDOWN:
						#Controls movement and power/angle adjustment
						if ((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)or (event.key == K_p)):
							if (self.side == 0):
								self.bluetank.adjust(event.key)
							elif (self.side == 1):
								self.redtank.adjust(event.key)
						if(event.key == K_SPACE):
							#Fire projectile and switch turn
							if (self.side == 0):
								self.side = 1
								bluetankpos = self.bluetank.rect.center
								self.reloadProjectiles([[bluetankpos[0], bluetankpos[1],self.bluetank.angle,self.bluetank.power,pygame.time.get_ticks(),'blue']])
							elif (self.side == 1):
								self.side = 0
								redtankpos = self.redtank.rect.center
								self.reloadProjectiles([[redtankpos[0], redtankpos[1],self.redtank.angle,self.redtank.power,pygame.time.get_ticks(), 'red']])
						#DEBUG ONLY - shows tank hitbox
						if(event.key == K_CAPSLOCK):
							pygame.draw.rect(self.background, (0,0,255),self.bluetank.rect)
							pygame.draw.rect(self.background, (255,0,0),self.redtank.rect)
						if(event.key == K_t):
							if(self.side ==0):
								for projectile in self.projectile:
									projectile.setTarget(self.bluetank.rect.center[0], self.bluetank.rect.center[1])
									projectile.doTrack = True
							else:
								for projectile in self.projectile:
									projectile.setTarget(self.redtank.rect.center[0], self.redtank.rect.center[1])
									projectile.doTrack = True

						if(event.key == K_s):
							for projectile in self.projectile:
								newprojectiles = projectile.split()
							self.reloadProjectiles(newprojectiles)
							for projectile in self.projectile:
								projectile.damage /=2
								
				#Smooth movement, power, and angle handling
				keys = pygame.key.get_pressed()
				if keys[K_p]:
					if (self.side == 0):
						self.bluetank.adjust(K_p)
					elif (self.side == 1):
						self.redtank.adjust(K_p)
				if keys[K_LEFT] or keys[K_RIGHT]:
					if (self.side == 0) and keys[K_LEFT]:
						self.bluetank.adjust(K_LEFT)
					elif (self.side == 1) and keys[K_LEFT]:
						self.redtank.adjust(K_LEFT)
					elif (self.side == 0) and keys[K_RIGHT]:
						self.bluetank.adjust(K_RIGHT)
					elif (self.side == 1) and keys[K_RIGHT]:
						self.redtank.adjust(K_RIGHT)
				if keys[K_UP] or keys[K_DOWN]:
					if (self.side == 0) and keys[K_DOWN]:
						self.bluetank.adjust(K_DOWN)
					elif (self.side == 1) and keys[K_DOWN]:
						self.redtank.adjust(K_DOWN)
					elif (self.side == 0) and keys[K_UP]:
						self.bluetank.adjust(K_UP)
					elif (self.side == 1) and keys[K_UP]:
						self.redtank.adjust(K_UP)
				
				#Rendering stuff
				self.redtank_sprite.clear(self.screen,self.background)
				self.bluetank_sprite.clear(self.screen,self.background)
				for sprites in self.projectile_sprites:
					sprites.clear(self.screen,self.background)
				self.redtank_sprite.draw(self.screen)
				self.bluetank_sprite.draw(self.screen)
				for projectile in self.projectile:
					projectile.domove()
				for sprites in self.projectile_sprites:
					sprites.draw(self.screen)
				pygame.display.flip()
				current = pygame.time.get_ticks()
				#WIP Collision Detection
				for projectile in self.projectile:
					if projectile.rect.colliderect(self.bluetank.rect) and projectile.color == 'red':
						self.bluetank.health -= projectile.damage
						print("Blue Tank Hit for " + str(projectile.damage) + " damage. New HP: " + str(self.bluetank.health))
						projectile.kill()
						self.projectile.remove(projectile)
					if projectile.rect.colliderect(self.redtank.rect) and projectile.color == 'blue':
						self.redtank.health -= projectile.damage
						print("Red Tank Hit for " + str(projectile.damage) + " damage. New HP: " + str(self.redtank.health))
						projectile.kill()
						self.projectile.remove(projectile)

	def LoadSprites(self):
	#Handles sprites
		self.bluetank = Tank.Tank(side=0)
		self.redtank = Tank.Tank(side=1)
		self.bluetank_sprite = pygame.sprite.RenderPlain((self.bluetank))
		self.redtank_sprite = pygame.sprite.RenderPlain((self.redtank))
		self.projectile = [Projectile.Projectile(99999, 99999, 0, 5, pygame.time.get_ticks(), "red")]
		self.projectile_sprites = []
		for projectile in self.projectile:
			self.projectile_sprites.append(pygame.sprite.RenderPlain(projectile))
	
	def reloadProjectiles(self,projectileList):
		for item in self.projectile:
			item.kill()
		for sprites in self.projectile_sprites:
				sprites.clear(self.screen,self.background)
		self.projectile = []
		self.projectile_sprites = []
		for projparams in projectileList:
			self.projectile.append(Projectile.Projectile(projparams[0],projparams[1],projparams[2],projparams[3],projparams[4],projparams[5]))
		for projectile in self.projectile:
			self.projectile_sprites.append(pygame.sprite.RenderPlain((projectile)))
		for sprites in self.projectile_sprites:
			sprites.clear(self.screen,self.background)

#Starts game if run from command line
if __name__ == "__main__":
	MainWindow = TankMain()
	MainWindow.MainLoop()

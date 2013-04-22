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
								self.reloadProjectiles(bluetankpos[0], bluetankpos[1],self.bluetank.angle,self.bluetank.power,'blue')
							elif (self.side == 1):
								self.side = 0
								redtankpos = self.redtank.rect.center
								self.reloadProjectiles(redtankpos[0], redtankpos[1],self.redtank.angle,self.bluetank.power, 'red')
						#DEBUG ONLY - shows tank hitbox
						if(event.key == K_CAPSLOCK):
							pygame.draw.rect(self.background, (0,0,255),self.bluetank.rect)
							pygame.draw.rect(self.background, (255,0,0),self.redtank.rect)
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
				self.projectile_sprites.clear(self.screen,self.background)
				self.redtank_sprite.draw(self.screen)
				self.bluetank_sprite.draw(self.screen)
				self.projectile.domove()
				self.projectile_sprites.draw(self.screen)
				pygame.display.flip()
				current = pygame.time.get_ticks()
				#WIP Collision Detection
				if self.projectile.rect.colliderect(self.bluetank.rect) and self.projectile.color == 'red':
					print("Blue Tank Hit")
					self.projectile.kill()
				if self.projectile.rect.colliderect(self.redtank.rect) and self.projectile.color == 'blue':
					print("Red Tank Hit")
					self.projectile.kill()

	def LoadSprites(self):
	#Handles sprites
		self.bluetank = Tank.Tank(side=0)
		self.redtank = Tank.Tank(side=1)
		self.bluetank_sprite = pygame.sprite.RenderPlain((self.bluetank))
		self.redtank_sprite = pygame.sprite.RenderPlain((self.redtank))
		self.projectile = Projectile.Projectile(100, 100, 0, 5, pygame.time.get_ticks(), "red")
		self.projectile_sprites = pygame.sprite.RenderPlain((self.projectile))
	
	def reloadProjectiles(self,x,y,angle,power, color):
		self.projectile = Projectile.Projectile(x,y,angle,power, pygame.time.get_ticks(), color)
		self.projectile_sprites = pygame.sprite.RenderPlain((self.projectile))
		self.projectile_sprites.clear(self.screen,self.background)

#Starts game if run from command line
if __name__ == "__main__":
	MainWindow = TankMain()
	MainWindow.MainLoop()

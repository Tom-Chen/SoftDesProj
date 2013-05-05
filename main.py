import os
import sys
import pygame
from pygame.locals import *
import Tank
import Text
import Projectile
import Terrain
import math

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
global MAXSPEED # Max projectile power
MAXSPEED = 150
global WIDTH
WIDTH = 1280
global HEIGHT
HEIGHT = 720

class TankMain():

	#Initializes game
	def __init__(self, width=WIDTH,height=HEIGHT):
		pygame.init()
		#Screen stuff
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(SKY, rect=None, special_flags=0)
		#Surfaces for clearing old values
		self.skyground = pygame.Surface((self.width,self.height))
		self.skyground.fill(SKY ,rect=None, special_flags=0)
		self.groundground = pygame.Surface((self.width,self.height))
		self.groundground.fill(GROUND ,rect=None, special_flags=0)
		pygame.display.set_caption('Tank!')
		
		#Red turn first
		self.side = 1
		
		#Checks for fonts
		if pygame.font:
			self.font = pygame.font.Font(None, 25)

		#Load stuff
		self.LoadTerrain()
		self.loadSprites()
		self.initText()

	def MainLoop(self):
	#Primary loop/event queue
		current = pygame.time.get_ticks()
		firetime = -3200
		while 1:
			#FPS and gamespeed limiter
			if(pygame.time.get_ticks()-current>(1000/FPS)):
				#Victory condition
				if(self.bluetank.health == 0):
					print("Red Tank wins. Congratulations!")
					sys.exit()
				if(self.redtank.health == 0):
					print("Blue Tank wins. Congratulations!")
					sys.exit()
				for event in pygame.event.get():
					#Quit
					if event.type == pygame.QUIT: 
						sys.exit()
					elif event.type == KEYDOWN and (pygame.time.get_ticks() - firetime > 3200):
						#Controls movement and power/angle adjustment
						if((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)or (event.key == K_p)):
							if (self.side == 0):
								self.bluetank.adjust(event.key)
							elif (self.side == 1):
								self.redtank.adjust(event.key)

						if(event.key == K_SPACE):
							#Fire projectile and switch turn
							bluetankpos = self.bluetank.rect.center
							redtankpos = self.redtank.rect.center
							firetime = pygame.time.get_ticks()
							if (self.side == 0):
								self.side = 1
								self.reloadProjectiles([[bluetankpos[0], bluetankpos[1],self.bluetank.angle,round(self.bluetank.power/5),pygame.time.get_ticks(),'blue',self.bluetank.fireMode,(redtankpos[0], redtankpos[1]) ]])
							elif (self.side == 1):
								self.side = 0
								if(self.redtank.ai):
									if self.redtank.moveBack:
										while(self.redtank.rect.center[0]<redtankpos[0] + 100):
											self.redtank.adjust(K_RIGHT)
										self.redtank.moveBack = False
									bluetankpos = self.bluetank.rect.center
									redtankpos = self.redtank.rect.center
									anglepower = self.getShot(redtankpos[0],bluetankpos[0],self.redtank.adjustshot)
									while(self.redtank.angle != 180+anglepower[0]):
										if self.redtank.angle > 180+anglepower[0]:
											self.redtank.adjust(K_DOWN)
										elif self.redtank.angle < 180+anglepower[0]:
											self.redtank.adjust(K_UP)
									while(self.redtank.power != anglepower[1]):
										self.redtank.adjust(K_p)
								self.reloadProjectiles([[redtankpos[0], redtankpos[1],self.redtank.angle,round(self.redtank.power/5),pygame.time.get_ticks(), 'red',self.redtank.fireMode,(bluetankpos[0], bluetankpos[1])]])

						#DEBUG ONLY - shows tank hitbox
						if(event.key == K_CAPSLOCK):

							pygame.draw.rect(self.skyground, (0,0,255),self.bluetank.rect)
							pygame.draw.rect(self.skyground, (255,0,0),self.redtank.rect)
							for terrain in self.terrain:
								pygame.draw.rect(self.skyground, (0,0,255),terrain.rect)



						# if(event.key == K_t):
							# if(self.side ==0):
								# for projectile in self.projectile:
									# projectile.setTarget(self.bluetank.rect.center[0], self.bluetank.rect.center[1])
									# projectile.doTrack = True
									# projectile.damage /=2
							# else:
								# for projectile in self.projectile:
									# projectile.setTarget(self.redtank.rect.center[0], self.redtank.rect.center[1])
									# projectile.doTrack = True
									# projectile.damage /=2
						if(event.key == K_2):
							if self.side == 1:
								self.redtank.fireMode = 2
								self.redtank.weapon = "Tracking"
							if self.side == 0:
								self.bluetank.fireMode = 2
								self.bluetank.weapon = "Tracking"
							print("Fire mode: Target")
						if(event.key == K_4):
							if self.side == 1:
								self.redtank.fireMode = 4
								self.redtank.weapon = "Hitscan"
							if self.side == 0:
								self.bluetank.fireMode = 4
								self.bluetank.weapon = "Hitscan"
							print("Fire mode: HitScan")
						if(event.key == K_3):
							if self.side == 1:
								self.redtank.fireMode = 3
								self.redtank.weapon = "Split"
							if self.side == 0:
								self.bluetank.fireMode = 3
								self.bluetank.weapon = "Split"
							print("Fire mode: Split")
						if(event.key == K_1):
							if self.side == 1:
								self.redtank.fireMode = 1
								self.redtank.weapon = "Normal"
							if self.side == 0:
								self.bluetank.fireMode = 1
								self.bluetank.weapon = "Normal"
							print("Fire mode: Normal")
						# if(event.key == K_s):
							# newprojectiles = []
							# for projectile in self.projectile:
								# #newprojectiles = projectile.split()
								# for params in projectile.split():
									# newprojectiles.append(params)
							# self.reloadProjectiles(newprojectiles)
							# for projectile in self.projectile:
								# projectile.damage /=4
						# if event.key == K_h:
							# for projectile in self.projectile:
								# projectile.hitScanEnable()
								
				#Smooth movement, power, and angle handling
				keys = pygame.key.get_pressed()
				if(pygame.time.get_ticks() - firetime > 3200):
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

				#Update text
				self.bluetext["power"].refresh(self.bluetank.power)
				self.bluetext["angle"].refresh(360-self.bluetank.angle)
				self.bluetext["shots"].refresh(self.bluetank.weapon)
				self.bluetext["armor"].refresh(self.bluetank.health)

				self.redtext["power"].refresh(self.redtank.power)
				self.redtext["angle"].refresh(self.redtank.angle-180)
				self.redtext["shots"].refresh(self.redtank.weapon)
				self.redtext["armor"].refresh(self.redtank.health)

				#Clearing old sprites
				self.redtank_sprite.clear(self.screen,self.skyground)
				self.bluetank_sprite.clear(self.screen,self.skyground)
				for sprite in self.bluetext_sprites:
					sprite.clear(self.screen,self.groundground)
				for sprite in self.redtext_sprites:
					sprite.clear(self.screen,self.groundground)
				for sprite in self.projectile_sprites:
					sprite.clear(self.screen,self.skyground)
				
				#Rendering new frame
				for sprite in self.bluetext_sprites:
					sprite.draw(self.screen)
				for sprite in self.redtext_sprites:
					sprite.draw(self.screen)
				self.redtank_sprite.draw(self.screen)
				self.bluetank_sprite.draw(self.screen)
				for projectile in self.projectile:
					projectile.domove()
					if projectile.splitMain:
						newprojectiles = []
						for projectile in self.projectile:
							#newprojectiles = projectile.split()
							for params in projectile.split():
								newprojectiles.append(params)
							self.reloadProjectiles(newprojectiles)
							for projectile in self.projectile:
								projectile.damage /=4
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
					for terrain in self.terrain:
						if projectile.rect.colliderect(terrain.rect):
							if projectile in self.projectile:
								print("Terrain Hit")
								if projectile.color == 'red':
									self.redtank.adjustshot += 1
								if projectile.color == 'blue':
									self.bluetank.adjustshot += 1
								projectile.kill()
								self.projectile.remove(projectile)
					if self.redtank.adjustshot >2:
						self.redtank.adjustshot = 0
						self.redtank.moveBack = True
					if self.bluetank.adjustshot > 2:
						self.bluetank.adjusthsot = 0
						#move back

	def loadSprites(self):
		#Tanks
		self.bluetank = Tank.Tank(side=0)
		self.redtank = Tank.Tank(side=1)
		self.bluetank_sprite = pygame.sprite.RenderPlain((self.bluetank))
		self.redtank_sprite = pygame.sprite.RenderPlain((self.redtank))

		#Text
		self.bluetext = {"power": Text.Text(self.bluetank.power,self.font,BLUE,(80,680)),
										"angle": Text.Text((450-self.bluetank.angle),self.font,BLUE,(80,660)),
										"shots": Text.Text(self.bluetank.weapon,self.font,BLUE,(80,640)),
										"armor": Text.Text(self.bluetank.health,self.font,BLUE,(80,620))}
		self.bluetext_sprites = []
		for value in self.bluetext.keys():
			self.bluetext_sprites.append(pygame.sprite.RenderPlain(self.bluetext[value]))

		self.redtext = {"power": Text.Text(self.redtank.power,self.font,RED,(1160,680)),
										"angle": Text.Text((self.redtank.angle-180),self.font,RED,(1160,660)),
										"shots": Text.Text(self.redtank.weapon,self.font,RED,(1160,640)),
										"armor": Text.Text(self.redtank.health,self.font,RED,(1160,620))}
		self.redtext_sprites = []
		for value in self.redtext.keys():
			self.redtext_sprites.append(pygame.sprite.RenderPlain(self.redtext[value]))

		#Projectiles
		self.projectile = [Projectile.Projectile(99999, 99999, 0, 5, pygame.time.get_ticks(), "red",0,(0,0))]
		self.projectile_sprites = []
		for projectile in self.projectile:
			self.projectile_sprites.append(pygame.sprite.RenderPlain(projectile))

	def LoadTerrain(self):
		self.terrain = [Terrain.Terrain(640,656,'ground'), Terrain.Terrain(640,418,'mount2')]
		self.terrain_sprites = []
		for terrain in self.terrain:
			self.terrain_sprites.append(pygame.sprite.RenderPlain(terrain))
		for terrain in self.terrain_sprites:
			terrain.draw(self.screen)

	def reloadProjectiles(self,projectileList):
		for item in self.projectile:
			item.kill()
		for sprites in self.projectile_sprites:
				sprites.clear(self.screen,self.skyground)
		self.projectile = []
		self.projectile_sprites = []
		for projparams in projectileList:
			self.projectile.append(Projectile.Projectile(projparams[0],projparams[1],projparams[2],projparams[3],projparams[4],projparams[5],projparams[6],projparams[7]))
		for projectile in self.projectile:
			self.projectile_sprites.append(pygame.sprite.RenderPlain((projectile)))
		for sprites in self.projectile_sprites:
			sprites.clear(self.screen,self.skyground)
			
	def getShot(self,xpos,xenemy,xadjust):
		angle = 30 + xadjust*15
		
		if xadjust>0:
			angle +=15
		if angle >89:
			angle = 89
		dx = math.fabs(xpos-xenemy)
		v = int(math.sqrt(dx*(1000/FPS)/(math.sin(2*math.radians(angle))))*.77)
		if v>MAXSPEED:
			v=MAXSPEED
		return (angle,v)

	def initText(self):	
		blupow = self.font.render("Power:", 1, BLUE)
		self.screen.blit(blupow, blupow.get_rect(left=(20),top=(680)))
		bluang = self.font.render("Angle:", 1, BLUE)
		self.screen.blit(bluang, bluang.get_rect(left=(20),top=(660)))
		bluwep = self.font.render("Shots:", 1, BLUE)
		self.screen.blit(bluwep, bluwep.get_rect(left=(20),top=(640)))
		bluhp = self.font.render("Armor:", 1, BLUE)
		self.screen.blit(bluhp, bluhp.get_rect(left=(20),top=(620)))
		
		redpow = self.font.render("Power:", 1, RED)
		self.screen.blit(redpow, redpow.get_rect(left=(1100),top=(680)))
		redang = self.font.render("Angle:", 1, RED)
		self.screen.blit(redang, redang.get_rect(left=(1100),top=(660)))
		redwep = self.font.render("Shots:", 1, RED)
		self.screen.blit(redwep, redwep.get_rect(left=(1100),top=(640)))
		redhp = self.font.render("Armor:", 1, RED)
		self.screen.blit(redhp, redhp.get_rect(left=(1100),top=(620)))

#Starts game if run from command line
if __name__ == "__main__":
	MainWindow = TankMain(1280,720)
	MainWindow.MainLoop()

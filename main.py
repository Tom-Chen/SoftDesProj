import os
import sys
import pygame
from pygame.locals import *

class TankMain():
  #Initializes game
    
  def __init__(self, width=800,height=600):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('Tank! Game!')
        
  def MainLoop(self):
    #Primary loop/event queue
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()
      pygame.display.update()

#Starts game if run from command line
if __name__ == "__main__":
  MainWindow = TankMain()
  MainWindow.MainLoop()
  
# class Tank():
  
# class Terrain():
  
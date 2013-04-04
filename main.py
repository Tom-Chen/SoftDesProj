import os
import sys
import pygame
from pygame.locals import *

class TankMain:
  #Initializes game
    
  def __init__(self, width=640,height=480):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
        
  def MainLoop(self):
    #Primary loop/event queue
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()

#Starts game if run from command line
if __name__ == "__main__":
  MainWindow = TankMain()
  MainWindow.MainLoop()
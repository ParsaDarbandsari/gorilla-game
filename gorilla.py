from game_object import GameObject
import pygame
import time

class Gorilla(GameObject):
	def __init__(self, screen, left, top):
		self.top = top
		self.left = left
		self.screen = screen
		self.pos = (left, top)
		super(Gorilla, self).__init__('gorilla', screen, self.pos)
	
	def idle(self):
		# Get image from the source
		img = pygame.image.load("sprites\\gorilla-idle.png").convert_alpha()
		
		self.screen.blit(img, self.pos)
	
	def throw(self):
		# Get image from the source
		img = pygame.image.load("sprites\\gorilla-throwing.png").convert_alpha()
		
		
		self.screen.blit(img, self.pos)
		# Throw banana(unimplemented feature)
		time.sleep(2/3)
		self.idle()
	
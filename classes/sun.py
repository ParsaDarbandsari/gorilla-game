from classes.game_object import GameObject
from classes.rect import Rect
import pygame


class Sun(GameObject):
	def __init__(self, screen, rect: Rect):
		super(Sun, self).__init__(screen, rect)
		self.idle()
	
	def idle(self):
		img = pygame.image.load("sprites\\sun-idle.png").convert_alpha()
		
		self.screen.blit(img, self.pos)
	
	def hit(self):
		img = pygame.image.load("sprites\\sun-hit.png").convert_alpha()
		
		self.screen.blit(img, self.pos)

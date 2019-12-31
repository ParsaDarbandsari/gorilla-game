from game_object import GameObject
from random import randint
from pygame import draw

class Building(GameObject):
	colors = ((0x00, 0x55, 0xdd), (0xcf, 0xcf, 0xcf), (0xcf, 0x00, 0x00))
	
	def __init__(self, screen, top, left, width, height):
		self.top_left = (top, left)
		self.width_height = (width, height)
		super(Building, self).__init__('Building', screen, self.top_left)
	
	def draw(self):
		rect = self.top_left + self.width_height
		draw.rect(self.screen, self.colors[randint(0, len(self.colors) - 1)], rect)

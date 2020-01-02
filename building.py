from game_object import GameObject
from random import randint
from pygame import draw

class Building(GameObject):
	def __init__(self, screen, top, left, width, height, building_color):
		self.top = top
		self.left = left
		self.width = width
		self.height = height
		self.building_color = building_color
		super(Building, self).__init__('Building', screen, (self.top, self.left))
	
	def draw(self):
		# Generate the body of the building
		rect = (self.top, self.left, self.width, self.height)
		draw.rect(self.screen, self.building_color, rect)
		
		# Add in the windows
		window_width = 8
		window_height = 13
		x_margin = 5
		y_margin = 5
		x_window_count = self.width // (window_width + x_margin)
		y_window_count = self.height // (window_height + y_margin)
		x_gap = ((self.width - x_margin) / x_window_count) - window_width
		y_gap = ((self.height - y_margin) / y_window_count) - window_height
		
		point_x = self.left + x_gap
		point_y = self.top + y_gap
		
		for y in range(y_window_count):
			for x in range(x_window_count):
				window_rect = (int(point_x + (x_gap + window_width) * x), int(point_y + (y_gap + window_height) * y), window_width, window_height)
				draw.rect(self.screen, (0, 255, 255), window_rect)
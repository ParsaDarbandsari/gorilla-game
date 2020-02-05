from classes.game_object import GameObject
from classes.rect import Rect
from pygame import draw

class Building(GameObject):
	def __init__(self, screen, rect: Rect, building_color):
		self.rect = rect
		self.building_color = building_color
		super(Building, self).__init__(screen, self.rect.location)
	
	def draw(self):
		# Generate the body of the building
		draw.rect(self.screen, self.building_color, self.rect.tuple)
		
		# Add in the windows
		window_width = 8
		window_height = 13
		x_margin = 5
		y_margin = 5
		x_window_count = self.rect.width // (window_width + x_margin)
		y_window_count = self.rect.height // (window_height + y_margin)
		x_gap = ((self.rect.width - x_margin) / x_window_count) - window_width
		y_gap = ((self.rect.height - y_margin) / y_window_count) - window_height
		
		point_x = self.rect.left + x_gap
		point_y = self.rect.top + y_gap
		
		for y in range(y_window_count):
			for x in range(x_window_count):
				window_rect = (int(point_x + (x_gap + window_width) * x), int(point_y + (y_gap + window_height) * y), window_width, window_height)
				draw.rect(self.screen, (0xf9, 0xa6, 0x02), window_rect)
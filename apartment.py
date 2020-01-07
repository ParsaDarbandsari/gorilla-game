from rect import Rect

class Apartment(object):
	def __init__(self, rect: Rect, color):
		self.__rect = rect
		self.__color = color
		
	@property
	def rect(self):
		return self.__rect
	
	@property
	def color(self):
		return self.__color
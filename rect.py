class Rect(object):
	def __init__(self, left, top, width, height):
		self.__top = top
		self.__left = left
		self.__width = width
		self.__height = height
	
	@property
	def tuple(self):
		return self.__left, self.__top, self.__width, self.__height
	
	@property
	def location(self):
		return self.__top, self.__left
	
	@property
	def width(self):
		return self.__width
	
	@property
	def height(self):
		return self.__height
	
	@property
	def left(self):
		return self.__left
	
	@property
	def top(self):
		return self.__top

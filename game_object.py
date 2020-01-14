class GameObject(object):
	def __init__(self, object_name, displaying_screen, position):
		self.name = object_name
		self.screen = displaying_screen
		self.pos = position

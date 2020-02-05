import math
from classes.building import Building


def generate_building(screen, rect, color):
	building = Building(screen, rect, color)
	building.draw()
	
def motion(angle, velocity, t, x, y, screen_height):
	g = 9.81
	vx = velocity * math.cos(math.radians(angle))
	vy = velocity * math.sin(math.radians(angle))
	X = vx * t
	Y = screen_height - (vy*t -(g/2)*t*t)

	return (X, Y)
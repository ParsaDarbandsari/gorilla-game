from building import Building


def generate_building(screen, top, left, width, height, color):
	building = Building(screen, top, left, width, height, color)
	building.draw()

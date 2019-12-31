from building import Building


def generate_building(screen, top, left, width, height):
	building = Building(screen, top, left, width, height)
	building.draw()

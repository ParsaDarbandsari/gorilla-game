from random import randint
from utils import *
import pygame
import time

# Initializing pygame
pygame.init()

# The colors
building_colors = ((0x00, 0x55, 0xdd), (0xcf, 0xcf, 0xcf), (0xcf, 0x00, 0x00))
window_colors = ((0xf9, 0xa6, 0x02), (0x69, 0x69, 0x69))

# Setting up the screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (0x00, 0x8d, 0xff)
TITLE = 'Gorilla Game'

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.DOUBLEBUF, 32)

# The Mainloop
done = False
while not done:
	screen.fill(BACKGROUND_COLOR)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	generate_building(screen, 10, 10, 120, 200, (255, 0, 0))
	pygame.display.update()
	time.sleep(1/60)


# And finally quiting
pygame.quit()

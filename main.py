from random import randint
from utils import *
import pygame

# Initializing pygame
pygame.init()

# Setting up the screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)
TITLE = 'Gorilla Game'

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.DOUBLEBUF, 32)

# The Mainloop
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((0x00, 0x8d, 0xff))
	generate_building(screen, 0, randint((SCREEN_HEIGHT // 2) - 80, (SCREEN_HEIGHT // 2) + 80), SCREEN_WIDTH // 7, SCREEN_HEIGHT)
	pygame.display.update()
	
	


# And finally quiting
pygame.quit()

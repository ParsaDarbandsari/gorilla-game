import pygame

# Initialize pygame
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


# And finally quiting
pygame.quit()

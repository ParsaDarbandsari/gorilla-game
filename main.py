from random import randint
from rect import Rect
from apartment import Apartment
from utils import *
import pygame
import time
import os

# Initializing pygame
pygame.init()

# The colors
building_colors = ((0x00, 0x55, 0xdd), (0xcf, 0xcf, 0xcf), (0xcf, 0x00, 0x00))
window_colors = ((0xf9, 0xa6, 0x02), (0x69, 0x69, 0x69))

APARTMENT_MIN_WIDTH = 90
APARTMENT_MAX_WIDTH = 120
APARTMENT_MIN_HEIGHT = 200
APARTMENT_MAX_HEIGHT = 350


# Setting up the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (0x00, 0x8d, 0xff)
TITLE = 'Gorilla Game'

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.DOUBLEBUF, 32)

apartments = []

for i in range(SCREEN_WIDTH // APARTMENT_MIN_WIDTH):
	w = randint(APARTMENT_MIN_WIDTH, APARTMENT_MAX_WIDTH)
	h = randint(APARTMENT_MIN_HEIGHT, APARTMENT_MAX_HEIGHT)
	t = SCREEN_HEIGHT - h
	if i > 0:
		l += apartments[i-1].rect.width
	else:
		l = 0
	a = Rect(l, t, w, h)
	c = (randint(0, 255), randint(0, 255), randint(0, 255))
	ap = Apartment(a, c)
	apartments.append(ap)

gorilla_idle = pygame.image.load("sprites\\gorilla-idle.jpg").convert()
gorilla_throwing = pygame.image.load("sprites\\gorilla-throwing.jpg").convert()

# The Mainloop
done = False
while not done:
	screen.fill(BACKGROUND_COLOR)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
	
	for ap in apartments:
		generate_building(screen, ap.rect, ap.color)

	screen.blit(gorilla_idle, (apartments[1].rect.left + apartments[1].rect.width // 2 - 50/2, apartments[1].rect.top - 50))
	screen.blit(gorilla_idle, (apartments[-1].rect.left + apartments[-2].rect.width // 2 - 50/2, apartments[-2].rect.top - 50))
	pygame.display.update()
	time.sleep(1/60)


# And finally quiting
pygame.quit()

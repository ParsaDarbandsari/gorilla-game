from classes.apartment import Apartment
from random import randint
from classes.gorilla import Gorilla
from classes.rect import Rect
from utils import *
import pygame
import time

# Initializing pygame
pygame.init()

# Setting up the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
SCREEN_RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (0x00, 0x8d, 0xff)
TITLE = 'Gorilla Game'
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.DOUBLEBUF, 32)

# Additional props
building_colors = ((0x00, 0x55, 0xdd), (0xcf, 0xcf, 0xcf), (0xcf, 0x00, 0x00))
window_colors = ((0xf9, 0xa6, 0x02), (0x69, 0x69, 0x69))
gorilla_idle = pygame.image.load("sprites\\gorilla-idle.png").convert_alpha()
gorilla_throwing = pygame.image.load("sprites\\gorilla-throwing.png").convert_alpha()

# Drawing the apartments
APARTMENT_MIN_WIDTH = 90
APARTMENT_MAX_WIDTH = 120
APARTMENT_MIN_HEIGHT = 200
APARTMENT_MAX_HEIGHT = 400
apartments = []
apartments_width = []

l = 0
i = 0
while sum(apartments_width) < SCREEN_WIDTH:
	w = randint(APARTMENT_MIN_WIDTH, APARTMENT_MAX_WIDTH)
	h = randint(APARTMENT_MIN_HEIGHT, APARTMENT_MAX_HEIGHT)
	t = SCREEN_HEIGHT - h
	if i > 0:
		l += apartments[i-1].rect.width
	else:
		l = 0
	apartment_rect = Rect(l, t, w, h)
	color = (randint(0, 255), randint(0, 255), randint(0, 255))
	ap = Apartment(apartment_rect, color)
	apartments.append(ap)
	apartments_width.append(ap.rect.width)
	i += 1

# Summon the gorillas
gorilla_1 = Gorilla(screen, apartments[1].rect.left + apartments[1].rect.width // 2 - 60/2, apartments[1].rect.top - 60)
gorilla_2 = Gorilla(screen, apartments[-2].rect.left + apartments[-2].rect.width // 2 - 60/2, apartments[-2].rect.top - 60)

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
	
	gorilla_1.idle()
	gorilla_2.idle()
	
	for ap in apartments:
		generate_building(screen, ap.rect, ap.color)
	
	pygame.display.update()
	time.sleep(1/60)


# And finally quiting
pygame.quit()

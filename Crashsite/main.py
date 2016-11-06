import pygame
import sys
import random

from pygame.locals import *

pygame.init()

CLOCK = pygame.time.Clock()
WINDOW = pygame.display.set_mode((800, 495), 0, 32)
pygame.display.set_caption('Spaceship Crash')

CRASH = pygame.image.load('crash.jpg')
MOON_MASK = pygame.image.load('MoonMask.png')
SHIP = pygame.image.load('ship.png').convert_alpha()


class Moon:
    def __init__(self, moon_x_pos, moon_y_pos):
        self.moon_x_pos = moon_x_pos
        self.moon_y_pos = moon_y_pos
        self.moon = pygame.image.load('Moon.png')


def clamp_increase(color, increment):
    return max(0, min(color + increment, 255))

pygame.mouse.set_visible(True)
start_move = False
moon_obj = Moon(273, 75)
x = 0
y = 240
color_increase = 0
flip = False
FIRE_ARRAY = []

while True:
    WINDOW.blit(CRASH, (0, 0))
    WINDOW.blit(MOON_MASK, (261, 77))
    WINDOW.blit(moon_obj.moon, (moon_obj.moon_x_pos, moon_obj.moon_y_pos))
    WINDOW.blit(SHIP, (0, 0))
    MOUSE_POS = pygame.mouse.get_pos()
    mouse_x, mouse_y = MOUSE_POS

    while y < 350:
        current_pix = SHIP.get_at((x, y))
        current_location = (x, y)
        r, g, b, a = current_pix
        if 20 < r < 256 and 60 < g < 200 and b < 77 and a != 0:
            FIRE_ARRAY.append(current_location)
        if x == 790:
            x = 0
            y += 1
        x += 1
    for pixel in FIRE_ARRAY:
        pix_to_change = SHIP.get_at(pixel)
        r1, g1, b1, a1 = pix_to_change
        SHIP.set_at(pixel, (clamp_increase(r1, color_increase), g1, b1))
    random_increase = random.randrange(2, 10)
    if flip is False:
        color_increase += random_increase
    else:
        color_increase -= random_increase
    if color_increase > 100:
        flip = not flip
        color_increase = 0
    elif color_increase < -100:
        flip = not flip
        color_increase = 0

    if pygame.event.get(MOUSEBUTTONDOWN) and \
            moon_obj.moon_x_pos < mouse_x < moon_obj.moon_x_pos + 109 and \
            moon_obj.moon_y_pos < mouse_y < moon_obj.moon_y_pos + 109:
        start_move = not start_move
    elif moon_obj.moon_x_pos > -109 and start_move is True:
        moon_obj.moon_x_pos -= 1
    elif moon_obj.moon_x_pos == -109 and start_move is True:
        moon_obj.moon_x_pos = 909

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    CLOCK.tick(60)

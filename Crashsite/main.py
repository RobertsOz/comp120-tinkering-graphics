import pygame
import sys
import random

from pygame.locals import *

pygame.init()

Clock = pygame.time.Clock()
Window = pygame.display.set_mode((800, 495), 0, 32)
# Name Window
pygame.display.set_caption('Spaceship Crash')
# Load Images we will be using
Crash = pygame.image.load('crash.jpg')
# This is the moon mask covering the static moon
Moon_mask = pygame.image.load('MoonMask.png')
# This is the ship Mask so the moon can go behind it
Ship = pygame.image.load('ship.png').convert_alpha()


# Create the moon class and load the moon.
class Moon:
    def __init__(self, moon_x_pos, moon_y_pos):
        self.moon_x_pos = moon_x_pos
        self.moon_y_pos = moon_y_pos
        self.moon = pygame.image.load('Moon.png')


# Color doesn't accept a number bigger than 255 so we have to make it not go past 255
def clamp_increase(colour, increment):
    return max(0, min(colour + increment, 255))


# Make and array of the pixels we will be manipulating
def array_pixels(x, y):
    while y < 350:
        current_pix = Ship.get_at((x, y))
        current_location = (x, y)
        r, g, b, a = current_pix
        if 20 < r < 256 and 60 < g < 200 and b < 77 and a != 0:
            FIRE_ARRAY.append(current_location)
        if x == 790:
            x = 0
            y += 1
        x += 1

# Define array
FIRE_ARRAY = []
# Initialise the array_pixels that will save the locations of each Fire pixel inside FIRE_ARRAY
array_pixels(0, 240)
# Set mouse visible if it isn't visible based on program it is running on
pygame.mouse.set_visible(True)
# Moon moving boolean if False it is not moving
start_move = False
# assign a variable for our Moon class
moon_obj = Moon(273, 75)
# set color_increase to 0 so the color changes get saved
color_increase = 0
# flip boolean to indicate when the red values are going up or down on the fire
flip = False

print "Click the Moon to start its rotation and Click it again to stop it."
while True:
    # Print the static Crash Image
    Window.blit(Crash, (0, 0))
    # Print the moon mask on top of the static moon
    Window.blit(Moon_mask, (261, 77))
    # Print the Moon class object on top of the mask where the static moon would be
    Window.blit(moon_obj.moon, (moon_obj.moon_x_pos, moon_obj.moon_y_pos))
    # Print Ship last so the Moon can go behind it
    Window.blit(Ship, (0, 0))

    # Mouse position data
    MOUSE_POS = pygame.mouse.get_pos()
    # Split the date into x and y coordinates
    mouse_x, mouse_y = MOUSE_POS

    # The fire flicker effect, goes through only the pixels we will be changing
    for pixel in FIRE_ARRAY:
        pix_to_change = Ship.get_at(pixel)
        r1, g1, b1, a1 = pix_to_change
        Ship.set_at(pixel, (clamp_increase(r1, color_increase), g1, b1))
    # Choose a random number to increase the color by on top of the last increase
    random_increase = random.randrange(2, 10)
    if flip is False:
        color_increase += random_increase
    else:
        color_increase -= random_increase
    # flip when color increase is more than 100 for timing reasons, so it doesnt flicker too fast
    if color_increase > 100:
        flip = not flip
        color_increase = 0
    elif color_increase < -100:
        flip = not flip
        color_increase = 0

    # If detect mouse click while the mouse position is on top of the moon start moving the moon.
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
    Clock.tick(60)

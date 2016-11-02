import pygame,sys,time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 495), 0, 32)
pygame.display.set_caption('Spaceship Crash')
#Colors

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

crash = pygame.image.load('crash.jpg')
moon_mask = pygame.image.load('MoonMask.png')
ship = pygame.image.load('ship.png')

class Moon:
    def __init__(self, moon_x_pos, moon_y_pos):
        self.moon_x_pos = moon_x_pos
        self.moon_y_pos = moon_y_pos
        self.moon = pygame.image.load('Moon.png')

startMove = False
pygame.mouse.set_visible(True)

moon_obj = Moon(273,75)

while True:
    window.blit(crash, (0, 0))
    window.blit(moon_mask,(261,77))
    window.blit(moon_obj.moon,(moon_obj.moon_x_pos,moon_obj.moon_y_pos))
    window.blit(ship,(0,0))
    mousePos =  pygame.mouse.get_pos()
    mouse_x, mouse_y = mousePos

    if pygame.event.get(MOUSEBUTTONDOWN) and \
            mouse_x > moon_obj.moon_x_pos and mouse_x < moon_obj.moon_x_pos+109 and \
            mouse_y > moon_obj.moon_y_pos and mouse_y < moon_obj.moon_y_pos+109:
        startMove = not startMove
    elif moon_obj.moon_x_pos > -109 and startMove == True:
        moon_obj.moon_x_pos -= 1
    elif moon_obj.moon_x_pos == -109 and startMove == True:
        moon_obj.moon_x_pos = 909





    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
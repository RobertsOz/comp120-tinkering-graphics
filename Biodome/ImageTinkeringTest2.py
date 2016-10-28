import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mouse.set_visible(1)


window_width = 800
window_height = 600
window_size = (window_width, window_height)
R1 = 255
G1 = 255
B1 = 255
R2 = 200
G2 = 200
B2 = 200

screen = pygame.display.set_mode(window_size)
bg = pygame.image.load("Biodome.jpg").convert_alpha()

# pixelarray
for x in range(bg.get_width()):
        for y in range (bg.get_height()):
            if bg.get_at((x,y)) == ((R1,B1,G1)):
                bg.set_at((x,y), (255,255,255,0))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,0,0))
    screen.blit(bg, (0,0))

    pygame.display.update()
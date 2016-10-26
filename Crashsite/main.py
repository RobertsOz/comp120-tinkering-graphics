import pygame,sys,math
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((800, 495), 0, 32)
pygame.display.set_caption('Spaceship Crash')
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255,10)
RED = (255,0,0)
GREEN = (0,255,0,255)
BLUE = (0,0,255)

crash = pygame.image.load('crash.jpg')
x_pos = 0
y_pos = 0

while True:

    window.blit(crash,(0,0))
    layer1 = pygame.Surface((800,495)).convert_alpha()
    layer1.fill(WHITE)
    window.blit(layer1, (0, 0))

    pixArray = pygame.PixelArray(layer1)
    #pixArray[x_pos:100, y_pos:100] = window.map_rgb(GREEN)
    while y_pos < 495:
        if x_pos < 800:
            pixArray[x_pos, y_pos] = window.map_rgb(GREEN)
            x_pos += 1
        elif x_pos == 800:
            print "THIS happened"
            y_pos += 1
            x_pos = 0

    del pixArray



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

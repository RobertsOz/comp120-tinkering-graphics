import pygame, sys, math
from pygame.locals import *

pygame.init()
pygame.mouse.set_visible(1)

#setting window size
window_width = 1920
window_height = 1080
window_size = (window_width, window_height)
#name for screena and adding the picture
screen = pygame.display.set_mode(window_size)
bg = pygame.image.load("C:\Users\Kieran\Desktop\Tinkering\Biodome.jpg").convert_alpha()
screen.fill((255,0,0))
screen.blit(bg, (0, 0))
#setting name for pixel array
PixelArray = pygame.PixelArray(screen)
#defining classes for the algorithms which will change the image so  can call them later using keys
def purplesky():
    for x in range(window_width):
        for y in range(window_height):
            R = screen.get_at((x,y)).r
            G = screen.get_at((x,y)).g
            B = screen.get_at((x,y)).b
            if R > 230 and G > 230 and B > 230:
                screen.set_at((x,y), (221,160,221))
#pixelarrays above and below
def greypicture():
    for x in range(window_width):
        for y in range(window_height):
            R = screen.get_at((x,y)).r
            G = screen.get_at((x,y)).g
            B = screen.get_at((x,y)).b
            Grey = (R + G + B)/3
            PixelArray[x,y] = (Grey, Grey, Grey)

def pinktree():
    for x in range(window_width):
        for y in range(window_height):
            R = screen.get_at((x,y)).r
            G = screen.get_at((x,y)).g
            B = screen.get_at((x,y)).b
            if R < 50 and G < 100 and B < 80:
                screen.set_at((x,y), (238,130,238))

def blur():
    for x in range(window_width-1):
        for y in range(window_height-1):
            R = screen.get_at((x, y)).r
            G = screen.get_at((x, y)).g
            B = screen.get_at((x, y)).b

            R1 = screen.get_at((x+1,y)).r
            G1 = screen.get_at((x+1, y)).g
            B1 = screen.get_at((x+1, y)).b

            R2 = (R + R1)/2
            G2 = (G + G1)/2
            B2 = (B + B1)/2


            screen.set_at((x,y)(R2,G2,B2))


#using keys to call the classes
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                purplesky()
        if event.type == pygame.KEYDOWN:
            if event.key == K_t:
                greypicture()
        if event.type == pygame.KEYDOWN:
            if event.key == K_y:
                pinktree()
        if event.type == pygame.KEYDOWN:
            if event.key == K_u:
                blur()







    pygame.display.update()
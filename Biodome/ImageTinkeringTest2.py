import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


window_width = 1920
window_height = 1080
window_size = (window_width, window_height)

screen = pygame.display.set_mode(window_size)
bg = pygame.image.load("C:\Users\Kieran\Desktop\Tinkering\Biodome.jpg")
screen.fill((0,0,0))
screen.blit(bg (0,0))

while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

clock.tick(60)

pygame.display.flip()
pygame.display.update()
import pygame
import sys
import random

from pygame.locals import *

pygame.init()

Clock = pygame.time.Clock()
Window = pygame.display.set_mode((1229, 768), 0, 32)
pygame.display.set_caption('Spaceship Bridge')

Bridge = pygame.image.load("bridge.jpg")
Bridge_mask = pygame.image.load("bridge_mask.png")
Destination1 = pygame.image.load("dest1.png")
Destination2 = pygame.image.load("dest2.png")
Destination3 = pygame.image.load("dest3.png")
Destination4 = pygame.image.load("dest4.png")
image_list = [Destination1,Destination2,Destination3,Destination4]
Window.blit(Bridge,(0,0))
Window.blit(Bridge_mask,(0,0))

def travel():
    if image_list:
        random_image = random.choice(image_list)
        Window.blit(random_image,(0,0))
        Window.blit(Bridge_mask,(0,0))
        image_list.remove(random_image)
    else:
        print "Out of fuel"


while True:

    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                travel()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    Clock.tick(10)

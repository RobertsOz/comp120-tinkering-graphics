import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# Set Width and Height of the game window, based on the images We will be using
WIDTH = 1229
HEIGHT = 768

# Make window
Window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# Name our Window.
pygame.display.set_caption('Spaceship Bridge')

# Load Images we will be using
Bridge = pygame.image.load("bridge.jpg")
# This is the Ship without the windows
Bridge_mask = pygame.image.load("bridge_mask.png")
# These are the Destination backgrounds
Destination1 = pygame.image.load("dest1.png")
Destination2 = pygame.image.load("dest2.png")
Destination3 = pygame.image.load("dest3.png")
Destination4 = pygame.image.load("dest4.png")
# List them here to loop through later
image_list = [Destination1, Destination2, Destination3, Destination4]

# Print the original Image we used.
Window.blit(Bridge, (0, 0))


# This will initialise when Space is pressed
def travel():
    # If there are Destinations left this will run if out of destinations print "Out of fuel"
    if image_list:
        # Invert the colors by swapping R G B places
        for y in xrange(0, HEIGHT - 1):
            for x in xrange(0, WIDTH - 1):
                current_pix = Bridge_mask.get_at((x, y))
                r, g, b, a = current_pix
                Bridge_mask.set_at((x, y), (b, r, g, a))
        # Choose a random destination
        random_image = random.choice(image_list)
        # Print the random destination on screen
        Window.blit(random_image, (0, 0))
        # Print the Bridge without the windows
        Window.blit(Bridge_mask, (0, 0))
        # Remove the Destination we traveled to from the list.
        image_list.remove(random_image)
    else:
        print "Out of fuel"

# Print instructions
print "Press Space to Travel to a new Galaxy!"
while True:

    pygame.display.update()
    for event in pygame.event.get():
        # If Space is pressed execute travel()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                travel()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

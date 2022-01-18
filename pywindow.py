from cmath import rect
import pygame
import time
import random
from pygame.locals import *


def main():
    quit = False
    x = 0
    y = 0
    while not quit:
        window.fill((0, 0, 0))

        keypressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True

    # game logic
        player = rect(x, y, 50, 50)
        pygame.draw.rect(window, (255, 255, 255), player)
        pygame.display.update()
        # .update() or .flip() either works

        clock.tick(25)
        # tick speed/ frames per second


# ********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 800, 600                            # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main()
    pygame.quit()

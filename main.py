import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from config import *

from sprites.player import Player

# pygame setup
pygame.init()

screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

player = Player(screen, window_center[0] - 30, window_center[1] - 30, SPEED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    player.update()
    player.draw()

    pygame.display.flip()

    clock.tick(FPS)


# This is going to be my first attempt at making the main game, wish me luck.

import pygame
import sys
import math

# Mandatory start
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bunker Game")

# Colors
GREEN = (34, 139, 34)
BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
RED = (200, 0, 0)
OFFWHITE = (255, 255, 245)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

class Worm:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
    #
    # Move?
    # -
    # Apply Gravity?
    # -
    # Check Collision (with terrain)?
    # -
    # Draw?
    # - 
    
class Projectile:
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.vel_x = math.cos(angle) * power
        self.vel_y = -math.sin(angle) * power
        self.radius = 4
        self.active = True
    #
    # Update?
    # -
    # Explode?
    # -
    # Draw?
    # -

# 
# Seperate Terrain Class? It's going to be edited a lot.
# - 

def Game():
    # Maybe terrain defining here, as a first?
    return
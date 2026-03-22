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

# Loading of images
# Still having to adjust paths (from main folder)
player_img = pygame.image.load("../images/player.png").convert_alpha()
terrain_img = pygame.image.load("../images/terrain.png").convert_alpha()

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

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
    
    def apply_gravity(self):
        if not self.on_ground:
            self.vel_y += 0.5
            self.y += self.vel_y
    
    # might need to pass terrain variable here as well
    def check_collision(self):
        self.on_ground = False
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.vel_y = 0
            self.on_ground = True
        else:
            # Check terrain collision
            if terrain.get_at((int(self.x), int(self.y + self.radius)))[3] != 0:
                self.y -= 1
                self.vel_y = 0
                self.on_ground = True

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
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

class Terrain:
    def __init__(self):
        return

def Game():
    # Maybe terrain defining here, as a first?
    return
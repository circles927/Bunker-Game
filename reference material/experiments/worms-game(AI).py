import pygame
import sys
import math
# import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Worms 2 Clone")

# Colors
GREEN = (34, 139, 34)
BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Terrain surface (for destructible terrain)
terrain = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
terrain.fill((0, 0, 0, 0))
pygame.draw.rect(terrain, GREEN, (0, HEIGHT - 150, WIDTH, 150))

# Worm class
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

# Projectile class
class Projectile:
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.vel_x = math.cos(angle) * power
        self.vel_y = -math.sin(angle) * power
        self.radius = 4
        self.active = True

    def update(self):
        if not self.active:
            return
        self.vel_y += 0.3  # gravity
        self.x += self.vel_x
        self.y += self.vel_y

        # Collision with terrain
        if 0 <= int(self.x) < WIDTH and 0 <= int(self.y) < HEIGHT:
            if terrain.get_at((int(self.x), int(self.y)))[3] != 0:
                self.explode()
        else:
            self.active = False

    def explode(self):
        pygame.draw.circle(terrain, (0, 0, 0, 0), (int(self.x), int(self.y)), 20)
        self.active = False

    def draw(self):
        if self.active:
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# Game setup
worms = [Worm(200, HEIGHT - 200, WHITE), Worm(600, HEIGHT - 200, WHITE)]
current_worm = 0
projectiles = []

# Main loop
while True:
    screen.fill(BLUE)
    screen.blit(terrain, (0, 0))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot projectile
                angle = math.radians(45)
                power = 8
                worm = worms[current_worm]
                projectiles.append(Projectile(worm.x, worm.y, angle, power))

    # Update worms
    worm = worms[current_worm]
    worm.move(keys)
    worm.apply_gravity()
    worm.check_collision()

    # Update projectiles
    for p in projectiles:
        p.update()

    # Draw worms and projectiles
    for w in worms:
        w.draw()
    for p in projectiles:
        p.draw()

    pygame.display.flip()
    clock.tick(60)

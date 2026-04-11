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
player_img = pygame.image.load("reference material/images/player2.1.png").convert_alpha()
terrain_img = pygame.image.load("reference material/images/terrain.png").convert_alpha()

terrain_mask = pygame.mask.from_surface(terrain_img)

# Colors
GREEN = (34, 139, 34)
BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
RED = (200, 0, 0)
OFFWHITE = (255, 255, 245)
WHITE = (255, 255, 255)

terrain_pos = (0, 450)

# Clock
clock = pygame.time.Clock()

class Worm:
    def __init__(self, x, y, imgWorm):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 99
        self.footing = (0, 0)
        self.imgWorm = imgWorm
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
        # wormRect = self.imgWorm.get_rect(topleft=(self.x, self.y))
        self.on_ground = False
        self.footing = (self.x + self.width // 2, self.y + self.height)  # Point at the middle of the worm's feet

        mask_x = self.footing[0] - terrain_pos[0]
        mask_y = self.footing[1] - terrain_pos[1]

        if 0 <= mask_x < terrain_mask.get_size()[0] and 0 <= mask_y < terrain_mask.get_size()[1]:
            if terrain_mask.get_at((mask_x, mask_y)) == 1:
                self.y -= 1
                self.vel_y = 0
                self.on_ground = True  # 1 if solid, 0 if empty
            else:
                self.on_ground = False
        
        return 0

    def draw(self):
        screen.blit(self.imgWorm, (self.x, self.y))
    
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

worms = [Worm(100, 100, player_img), Worm(300, 100, player_img)]
current_worm = 0

while True:
    # Main Game loop
    # Starting by spawning two example worms
    screen.fill((75, 75, 255))
    screen.blit(terrain_img, terrain_pos)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Spacebar pressed - shoot projectile")
    
    worm = worms[current_worm]
    worm.move(keys)
    worm.apply_gravity()
    worm.check_collision()
    worm.draw()

    pygame.display.flip()
    clock.tick(60)
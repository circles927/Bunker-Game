import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Perfect Collision with Gravity")

# Clock for FPS control
clock = pygame.time.Clock()

# Colors
BG_COLOR = (135, 206, 235)  # Sky blue

# Load images with transparency
player_img = pygame.image.load("../images/player.png").convert_alpha()
terrain_img = pygame.image.load("../images/terrain.png").convert_alpha()

# Create rects
player_rect = player_img.get_rect(topleft=(100, 100))
terrain_rect = terrain_img.get_rect(topleft=(0, 450))

# Create masks for pixel-perfect collision
player_mask = pygame.mask.from_surface(player_img)
terrain_mask = pygame.mask.from_surface(terrain_img)

# Physics variables
gravity = 0.5
player_vel_y = 0
on_ground = False

def pixel_perfect_collision(rect1, mask1, rect2, mask2):
    """Check pixel-perfect collision between two masked surfaces."""
    offset = (rect2.x - rect1.x, rect2.y - rect1.y)
    overlap = mask1.overlap(mask2, offset)
    return overlap  # Returns None if no collision, else (x, y) tuple

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply gravity
    if not on_ground:
        player_vel_y += gravity
    else:
        player_vel_y = 0

    # Move player vertically
    player_rect.y += player_vel_y
    on_ground = False

    # Check collision with terrain
    if pixel_perfect_collision(player_rect, player_mask, terrain_rect, terrain_mask):
        # Move player up until no collision (simple resolution)
        while pixel_perfect_collision(player_rect, player_mask, terrain_rect, terrain_mask):
            player_rect.y -= 1
        on_ground = True

    # Drawing
    screen.fill(BG_COLOR)
    screen.blit(terrain_img, terrain_rect)
    screen.blit(player_img, player_rect)

    pygame.display.flip()
    clock.tick(60)

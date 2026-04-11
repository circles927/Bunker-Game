import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Mask Point Collision Example")

# Load terrain image (must have transparency for mask to work properly)
terrain_image = pygame.image.load("../images/terrain.png").convert_alpha()

# Create mask from terrain image
terrain_mask = pygame.mask.from_surface(terrain_image)

# Terrain position on screen
terrain_pos = (0, 450)  # top-left corner

# Function to check if a point collides with terrain
def point_hits_terrain(point_x, point_y):
    # Convert screen coordinates to mask coordinates
    mask_x = point_x - terrain_pos[0]
    mask_y = point_y - terrain_pos[1]

    # Check bounds before accessing mask
    if 0 <= mask_x < terrain_mask.get_size()[0] and 0 <= mask_y < terrain_mask.get_size()[1]:
        return terrain_mask.get_at((mask_x, mask_y))  # 1 if solid, 0 if empty
    return 0

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check collision
    hit = point_hits_terrain(mouse_x, mouse_y)

    # Draw background
    screen.fill((50, 50, 50))

    # Draw terrain
    screen.blit(terrain_image, terrain_pos)

    # Draw mouse point (red if hit, green if not)
    color = (255, 0, 0) if hit else (0, 255, 0)
    pygame.draw.circle(screen, color, (mouse_x, mouse_y), 5)

    pygame.display.flip()
    clock.tick(60)

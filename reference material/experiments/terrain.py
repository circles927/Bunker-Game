# This is where I'm supposed to make a first experiment with creating terrain, and blast radiuses etc...
# Starting with imports:
import pygame
# import json
# import sys

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Terrain Experiment")
    
    click_positions = []

    player_LOCX = 200  # Example player location
    player_LOCY = 200

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        
        # Draw some terrain (for example, a simple green rectangle)
        pygame.draw.rect(screen, (0, 255, 0), (0, 400, 800, 200), 0)
        
        terrain_mask = pygame.mask.from_threshold(screen, (0, 255, 0, 255), (0, 25, 0, 0))  # Create a mask from the current screen (for collision detection, etc.)

        pygame.draw.circle(screen, (255, 0, 0, 255), (player_LOCX, player_LOCY), 25, 0)  # Draw the player as a red circle

        player_mask = pygame.mask.from_threshold(screen, (255, 0, 0, 255), (25, 0, 0, 0)) 

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = pygame.mouse.get_pos()
            click_positions.append(mouse_pos)

        for pos in click_positions:
            pygame.draw.circle(screen, (0, 0, 0), pos, 50, 0)

            
        # circles_mask = pygame.mask.from_threshold(screen, (0, 0, 0, 255), (25, 25, 25, 255))

        # terrain_mask.erase(circles_mask, (0, 0))  # Erase the circles from the terrain mask

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

main()
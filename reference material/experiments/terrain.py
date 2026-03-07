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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = pygame.mouse.get_pos()
            click_positions.append(mouse_pos)

        for pos in click_positions:
            pygame.draw.circle(screen, (255, 255, 255), pos, 50, 0)

        # Update the display
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()

main()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Valentine's Day Graphics")

# Colors
red = (255, 0, 0)
white = (255, 255, 255)

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Draw heart shape
    pygame.draw.polygon(screen, red, [(300, 100), (500, 300), (300, 200), (100, 300)])

    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Happy Valentine's Day!", True, red)
    screen.blit(text, (150, 350))

    # Update display
    pygame.display.flip()

    # Set frames per second
    clock.tick(30)
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dancing Fish")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fish properties
fish_img = pygame.image.load("fish.png")
fish_rect = fish_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Load music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# Dance parameters
dance_moves = [(-10, 0), (10, 0), (0, -10), (0, 10)]
dance_timer = 0
dance_interval = 500  # milliseconds

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Dance logic
    current_time = pygame.time.get_ticks()
    if current_time - dance_timer > dance_interval:
        move = random.choice(dance_moves)
        fish_rect.move_ip(move)
        dance_timer = current_time

    # Draw fish
    screen.blit(fish_img, fish_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

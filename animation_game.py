import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 1500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_dx = 5   # speed in x direction
ball_dy = 5   # speed in y direction
ball_color = random.choice([RED, GREEN, BLUE, WHITE])

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1
        ball_color = random.choice([RED, GREEN, BLUE, WHITE])  # change color on bounce
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1
        ball_color = random.choice([RED, GREEN, BLUE, WHITE])

    # Fill background
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

pygame.quit()
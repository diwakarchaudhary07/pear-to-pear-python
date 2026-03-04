import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bike Race Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Bike setup
bike_width, bike_height = 50, 80
bike = pygame.Rect(WIDTH//2, HEIGHT-100, bike_width, bike_height)

# Obstacle setup
obstacle_width, obstacle_height = 50, 80
obstacles = []
speed = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

def draw_bike():
    pygame.draw.rect(screen, RED, bike)

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, BLACK, obs)

def show_message(text):
    msg = font.render(text, True, RED)
    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

# Game loop
running = True
score = 0

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bike.left > 0:
        bike.move_ip(-7, 0)
    if keys[pygame.K_RIGHT] and bike.right < WIDTH:
        bike.move_ip(7, 0)

    # Spawn obstacles
    if random.randint(1, 30) == 1:
        x_pos = random.randint(0, WIDTH - obstacle_width)
        obstacles.append(pygame.Rect(x_pos, -obstacle_height, obstacle_width, obstacle_height))

    # Move obstacles
    for obs in obstacles[:]:
        obs.move_ip(0, speed)
        if obs.top > HEIGHT:
            obstacles.remove(obs)
            score += 1

    # Collision detection
    for obs in obstacles:
        if bike.colliderect(obs):
            show_message("GAME OVER")
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    # Draw everything
    draw_bike()
    draw_obstacles()

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
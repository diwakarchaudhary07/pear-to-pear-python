import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display size
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Animation Game with Levels')

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10   # initial speed

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score, level):
    value = score_font.render("Score: " + str(score) + "  Level: " + str(level), True, black)
    dis.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def draw_walls():
    pygame.draw.rect(dis, black, [0, 0, dis_width, 10])   # Top
    pygame.draw.rect(dis, black, [0, dis_height-10, dis_width, 10])  # Bottom
    pygame.draw.rect(dis, black, [0, 0, 10, dis_height])  # Left
    pygame.draw.rect(dis, black, [dis_width-10, 0, 10, dis_height])  # Right

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0
    level = 1
    snake_speed = 10

    foodx = round(random.randrange(20, dis_width - 40) / 20.0) * 20.0
    foody = round(random.randrange(20, dis_height - 40) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Collision with walls
        if x1 >= dis_width-10 or x1 < 10 or y1 >= dis_height-10 or y1 < 10:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        draw_walls()
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(score, level)

        pygame.display.update()

        # ✅ Proper collision detection using Rect
        snake_rect = pygame.Rect(x1, y1, snake_block, snake_block)
        food_rect = pygame.Rect(foodx, foody, snake_block, snake_block)

        if snake_rect.colliderect(food_rect):
            foodx = round(random.randrange(20, dis_width - 40) / 20.0) * 20.0
            foody = round(random.randrange(20, dis_height - 40) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10

            if score % 50 == 0:
                level += 1
                snake_speed = int(snake_speed + 3)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
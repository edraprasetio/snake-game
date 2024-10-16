import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window dimensions
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Snake parameters
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Initial snake position
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_x_change = 0
snake_y_change = 0

# Food position
food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

# Clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        running = False

    window.fill(BLACK)
    
    # Draw food
    pygame.draw.rect(window, RED, [food_x, food_y, snake_block, snake_block])

    # Update snake body
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with itself
    for x in snake_list[:-1]:
        if x == snake_head:
            running = False

    draw_snake(snake_block, snake_list)

    # Detect collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
        snake_length += 1

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Snake Game 1.0')

snake = [(250, 350), (260, 350), (270, 350), (280, 350)]
snake_body1 = pygame.Surface((10, 10))
snake_body1.fill((0, 0, 0))
snake_body2 = pygame.Surface((10, 10))
snake_body2.fill((255, 0, 0))

direction = 'LEFT'
clock = pygame.time.Clock()

while True:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            def direction(i):
                switcher = {
                    K_UP: 'UP',
                    K_DOWN: 'DOWN',
                    K_LEFT: 'LEFT',
                    K_RIGHT: 'RIGHT'
                }
                return switcher.get(i, "LEFT")
            direction = direction(event.key)

    #makes the snake crawl
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    def crawl(i):
        switcher = {
            'UP': (snake[0][0], snake[0][1] - 10),
            'DOWN': (snake[0][0], snake[0][1] + 10),
            'LEFT': (snake[0][0] - 10, snake[0][1]),
            'RIGHT': (snake[0][0] + 10, snake[0][1])
        }
        return switcher.get(i, (snake[0][0] - 10, snake[0][1]))
    snake[0] = crawl(direction)

    screen.fill((255, 255, 255))

    for i in range(len(snake)):
        if i == 0:
            screen.blit(snake_body1, snake[i])
        else:
            screen.blit(snake_body2, snake[i])

    pygame.display.update()
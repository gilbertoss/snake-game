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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))

    for i in range(len(snake)):
        if i == 0:
            screen.blit(snake_body1, snake[i])
        else:
            screen.blit(snake_body2, snake[i])

    # for pos in snake:        
    #     screen.blit(snake_head, pos)
    pygame.display.update()
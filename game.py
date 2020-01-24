import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Snake Game 1.0')

while True:
    screen.fill((255, 255, 255))
    pygame.display.update()
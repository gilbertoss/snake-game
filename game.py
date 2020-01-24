import pygame, random
from pygame.locals import *

pygame.init()

def location_random():
    x = random.randint(0, screen_width - screen_grid)
    y = random.randint(0, screen_width - screen_grid)
    return (x//screen_grid * screen_grid, y//screen_grid * screen_grid)

def food_collision(obj1, obj2):
    return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

def boundaries_collision():
    return snake[0][0] == screen_width or snake[0][1] == screen_height or snake[0][0] < 0 or snake[0][1] < 0

def body_collision():
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True
    return False

def crawl(i):
    switcher = {
        'UP':    (snake[0][0], snake[0][1] - screen_grid),
        'DOWN':  (snake[0][0], snake[0][1] + screen_grid),
        'LEFT':  (snake[0][0] - screen_grid, snake[0][1]),
        'RIGHT': (snake[0][0] + screen_grid, snake[0][1])
    }
    return switcher.get(i, (snake[0][0] - 10, snake[0][1]))

def get_direction(i):
    switcher = {
        K_UP:    'UP',
        K_DOWN:  'DOWN',
        K_LEFT:  'LEFT',
        K_RIGHT: 'RIGHT'
    }
    return switcher.get(i, "LEFT")

screen_width = 500
screen_height = 700
screen_grid = 10
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game 1.0')

game_velocity = 5
font = pygame.font.SysFont('Kinnari.ttf', 30)
score = 0
game_over = False
direction = 'LEFT'
clock = pygame.time.Clock()

snake = [(250, 350), (260, 350), (270, 350), (280, 350)]
snake_body1 = pygame.Surface((screen_grid, screen_grid))
snake_body1.fill((0, 0, 0))
snake_body2 = pygame.Surface((screen_grid, screen_grid))
snake_body2.fill((107, 66, 38))

apple_location = location_random()
apple = pygame.Surface((screen_grid, screen_grid))
apple_collors = [(50,205,50), (255, 0, 0), (0, 0, 255)]
apple.fill(apple_collors[random.randint(0, len(apple_collors) - 1)])

while not game_over:
    clock.tick(game_velocity)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:            
            direction = get_direction(event.key)

    if food_collision(snake[0], apple_location):
        apple.fill(apple_collors[random.randint(0, len(apple_collors) - 1)])        
        apple_location = location_random()
        snake.append((0, 0))
        game_velocity += 1
        score += 1
    
    if boundaries_collision():
        game_over = True
        break
    
    if body_collision():
        game_over = True
        break

    if game_over:
        break

    #makes the snake crawl
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])    
    snake[0] = crawl(direction)

    screen.fill((255, 255, 255))

    screen.blit(apple, apple_location)

    for i in range(len(snake)):
        if i == 0:
            screen.blit(snake_body1, snake[i])
        else:
            screen.blit(snake_body2, snake[i])
    
    score_font = font.render('Score: %s' % (score), True, (0, 0, 0))
    score_rect = score_font.get_rect()
    score_rect.topleft = (screen_width - 120, 10)
    screen.blit(score_font, score_rect)

    pygame.display.update()

while True:
    game_over_font = pygame.font.SysFont('Kinnari.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 69, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 2)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
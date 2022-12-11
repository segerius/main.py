import pygame
from random import randrange
import sys

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
rcircle = (randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE))
dx, dy = 0, 0
snake = [(x, y)]
length = 1
fps = 60
speed_count, snake_speed = 0, 100
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

pygame.init()
screen = pygame.display.set_mode((RES, RES))
r = pygame.Rect(randrange(0, RES, SIZE), randrange(0, RES, SIZE), SIZE, SIZE)
img = pygame.image.load('81e07cd1623d223c425b85a0e18353b6.jpg').convert()
clock = pygame.time.Clock()
font_end = pygame.font.SysFont('Arial', 66, bold=True)


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)

    pygame.display.flip()


def game_over():
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()


while True:
    screen.blit(img, (0, 0))
    [pygame.draw.rect(screen, (255, 0, 0), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.circle(screen, 'green', rcircle, 25, 50)
    close_game()
    # snake movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
    # eating food
    if snake[-1] == rcircle:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        snake_speed -= 0
    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
    game_over()
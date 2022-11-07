import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

FPS = 30
# количество шариков одного вида
balls_number = 5
fast_balls_number = 5
# параметры экрана
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (75, 50, 150)
LIME = (7, 242, 46)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#списки с данными для шариков, координаты по x, y, радиус, скорость по x, скорость по y
x = [0] * balls_number
y = [0] * balls_number
radius = [0] * balls_number
velocity_x = [0] * balls_number
velocity_y = [0] * balls_number
color = [RED] * balls_number
x_1 = [0] * fast_balls_number
y_1 = [0] * fast_balls_number
radius_1 = [0] * fast_balls_number
velocity_x1 = [0] * fast_balls_number
velocity_y1 = [0] * fast_balls_number
color_1 = [RED] * fast_balls_number
score_color = LIME
#заготовка для отображения счёта
font_style = pygame.font.SysFont('arial', 36)
score_font = pygame.font.SysFont('arial', 36)


def your_score(score):
    '''
    рисует на экране счёт
    score - количество очков, полученных пользователем
    '''
    value = score_font.render('Счёт: ' + str(score), True, LIME)
    screen.blit(value, [0, 0])


def new_ball(n):
    '''
    добавляет данные для нового шарика
    n - индекс в массиве с списке
    '''
    global x, y, radius, velocity_x, velocity_y, color
    radius[n] = 40
    x[n] = randint(radius[n], width - radius[n])
    y[n] = randint(radius[n], height - radius[n])
    velocity_x[n] = (randint(0, 1) - 0.5) * 300 / FPS
    velocity_y[n] = (randint(0, 1) - 0.5) * 300 / FPS
    color[n] = COLORS[randint(0, 5)]


def new_fast_ball(n):
    '''
    добавляет данные для нового быстрого шарика
    n - индекс в списке
    '''
    global x_1, y_1, radius_1, velocity_x1, velocity_y1, color_1
    radius_1[n] = 20
    x_1[n] = randint(radius_1[n], width - radius_1[n])
    y_1[n] = randint(radius_1[n], height - radius_1[n])
    velocity_x1[n] = (randint(1, 2) - 0.5) * 300 / FPS
    velocity_y1[n] = (randint(1, 2) - 0.5) * 300 / FPS
    color_1[n] = COLORS[randint(0, 5)]


def draw_balls():
    '''
    отображает шарики в игре
    '''
    global x, y, radius, color, x_1, y_1, radius_1, color_1
    screen.fill(PURPLE)
    for i in range(balls_number):
        circle(screen, color[i], (x[i], y[i]), radius[i])
    for i in range(fast_balls_number):
        circle(screen, COLORS[randint(0, 5)], (x_1[i], y_1[i]), radius_1[i])


def click1(event):
    '''
    проверяет, попали ли по обычному шарику
    event - событие на экране (нажатие клавиши)
    '''
    global x, y, radius
    for i in range(balls_number):
        if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 <= radius[i] ** 2:
            return i
    return - 1


def click2(event):
    '''
    проверяет, попали ли по быстрому шарику
    event - событие на экране (нажатие клавиши)
    '''
    global x_1, y_1, radius_1
    for i in range(fast_balls_number):
        if (event.pos[0] - x_1[i]) ** 2 + (event.pos[1] - y_1[i]) ** 2 <= radius_1[i] ** 2:
            return i
    return - 1


def move_balls():
    '''
    перемещение шариков, рисует счёт в верхнем правом углу
    '''
    global x, y, radius, velocity_x, velocity_y, color, x_1, y_1, radius_1, velocity_x1, velocity_y1, color_1
    for i in range(balls_number):
        x[i] += velocity_x[i]
        y[i] += velocity_y[i]
    for i in range(fast_balls_number):
        x_1[i] += velocity_x1[i]
        y_1[i] += velocity_y1[i]
    draw_balls()
    your_score(score)
    pygame.display.update()


def get_scores1(n):
    '''
    увеличивает очки за пойманный обычный шарик, генерирует новый шарик после того, как его поймали
    n - индекс в массиве, пойманного шарика
    '''
    global score
    score += 10
    screen.fill(PURPLE)
    new_ball(n)
    draw_balls()
    pygame.display.update()


def get_scores2(n):
    '''
    увеличивает очки за пойманный быстрый шарик, генерирует новый шарик после того, как его поймали
    n - индекс в массиве, пойманного шарика
    '''
    global score
    score += 30
    screen.fill(PURPLE)
    new_fast_ball(n)
    draw_balls()
    pygame.display.update()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0
for i in range(balls_number):
    new_ball(i)
for i in range(fast_balls_number):
    new_fast_ball(i)
draw_balls()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            number_caught = click1(event)
            if number_caught != - 1:
                get_scores1(number_caught)
            number_caught = click2(event)
            if number_caught != - 1:
                get_scores2(number_caught)
            your_score(score)
    move_balls()
    #отражение шариков от границы
    for i in range(balls_number):
        if (x[i] - radius[i] < 0) or (x[i] + radius[i] > width):
            velocity_x[i] = - velocity_x[i]
        if (y[i] - radius[i] < 0) or (y[i] + radius[i] > height):
            velocity_y[i] = - velocity_y[i]
    for i in range(fast_balls_number):
        if (x_1[i] - radius_1[i] < 0) or (x_1[i] + radius_1[i] > width):
            velocity_x1[i] = - velocity_x1[i]
        if (y_1[i] - radius_1[i] < 0) or (y_1[i] + radius_1[i] > height):
            velocity_y1[i] = - velocity_y1[i]
pygame.quit()

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))

YELLOW = (225, 225, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)

screen.fill(GRAY)
circle(screen, BLACK, (450, 450), 201, 1)
circle(screen, YELLOW, (450, 450), 200)
rect(screen, BLACK, (350, 550, 200, 40))
circle(screen, RED, (350, 420), 36)
circle(screen, BLACK, (350, 420), 37, 1)
circle(screen, BLACK, (350, 420), 18)
circle(screen, RED, (550, 420), 30)
circle(screen, BLACK, (550, 420), 31, 1)
circle(screen, BLACK, (550, 420), 15)
for i in range(30):
    line(screen, BLACK, (480 - 1 / 4 * i, 420 - 1 / 2 * i),
         (650 - 1 / 4 * i, 335 - 1 / 2 * i), 2)
for i in range(15):
    line(screen, BLACK, (400 + 1 * i, 420 - i),
         (270 + 1 * i, 290 - i), 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

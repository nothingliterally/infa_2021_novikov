import pygame
import sys
from random import randint
from pygame.draw import *

pygame.init()
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BROWN = (100, 100, 0)
COLORS = [RED, BLUE, WHITE, GREEN, MAGENTA, CYAN, BLACK, BLACK, BLACK, BLACK, BLACK]

FPS = 60
Height = 800
# of play screen

Width = 1400
# of play screen

screen = pygame.display.set_mode((Width, Height))

x3 = randint(400, 900)
x1 = randint(200, 1100)
x2 = randint(200, 1100)
y3 = randint(400, 600)
y1 = randint(200, 600)
y2 = randint(200, 600)
r1 = randint(30, 70)
r2 = randint(30, 40)

speed = [randint(-4, 4), randint(-4, 4)]
speed1 = [randint(-4, 4), randint(-4, 4)]
speed2 = [randint(-4, 4), randint(-4, 4)]


# start speed of objects


def face(x, y):
    """
    Draws yellow Shrek (Yes, Yellow!) with centre (x, y)
    """
    pygame.draw.circle(screen, YELLOW, [x, y], 160)
    pygame.draw.line(screen, BROWN, [-150 + x, -150 + y], [-30 + x, -70 + y], 15)
    pygame.draw.line(screen, BROWN, [30 + x, -70 + y], [150 + x, -150 + y], 15)
    pygame.draw.circle(screen, BLACK, [-80 + x, -35 + y], 20)
    pygame.draw.circle(screen, RED, [-80 + x, -35 + y], 45, 25)
    pygame.draw.circle(screen, BLACK, [80 + x, -35 + y], 10)
    pygame.draw.circle(screen, RED, [80 + x, -35 + y], 45, 35)
    pygame.draw.circle(screen, BLACK, [40 + x, 55 + y], 35, 10)
    pygame.draw.line(screen, BLACK, [20 + x, 30 + y], [-50 + x, 60 + y], 10)
    pygame.draw.line(screen, BLACK, [60 + x, 75 + y], [x, 110 + y], 10)


def new_ball(x, y, r, color):
    if color == BLACK:
        circle(screen, color, (x, y), 0)
    else:
        circle(screen, color, (x, y), r)


run = True
counter = 0
# score counter

i = 0

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x3) ** 2 + (event.pos[1] - y3) ** 2 <= 80 ** 2:
            counter += 2
        # perfect hit on face

        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x3) ** 2 + (event.pos[1] - y3) ** 2 <= 160 ** 2:
            counter += 1
        # bad hit on face

        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2 <= (
                r1 // 2) ** 2:
            counter += 20
        # perfect hit on 1st circle

        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2 <= r1 ** 2:
            counter += 10
        # bad hit on 1st circle

        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x2) ** 2 + (event.pos[1] - y2) ** 2 <= (
                r2 // 2) ** 2:
            counter += 20
        # perfect hit on 2nd circle

        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x2) ** 2 + (event.pos[1] - y2) ** 2 <= r2 ** 2:
            counter += 10
        # bad hit on 2nd circle

    x3 += speed[0]
    y3 += speed[1]
    x1 -= speed1[0]
    y1 -= speed1[1]
    x2 -= speed2[0]
    y2 -= speed2[1]
    # moving our objects

    if x3 + 190 >= Width or x3 - 190 <= 0:
        if x3 + 190 >= Width:
            x3 = Width - 200
        elif x3 - 190 <= 0:
            x3 = 200
        speed[0] = -speed[0]
        speed[1] += randint(-3, 3)
    if y3 + 190 >= Height or y3 - 190 <= 0:
        if y3 + 190 >= Height:
            y3 = Height - 200
        elif y3 - 190 <= 0:
            y3 = 200
        speed[1] = -speed[1]
        speed[0] += randint(-3, 3)

    if x1 + r1 + 10 >= Width or x1 - r1 - 10 <= 0:
        if x1 + r1 + 10 >= Width:
            x1 = Width - r1 - 40
        elif x1 - r1 - 10 <= 0:
            x1 = r1 + 40
        speed1[0] = -speed1[0]
        speed1[1] += randint(-3, 3)
    if y1 + r1 + 10 >= Height or y1 - r1 - 10 <= 0:
        if y1 + r1 + 10 >= Height:
            y1 = Height - r1 - 40
        elif y1 - r1 - 10 <= 0:
            y1 = r1 + 40
        speed1[1] = -speed1[1]
        speed1[0] += randint(-3, 3)

    if x2 + r2 + 10 >= Width or x2 - r2 - 10 <= 0:
        if x2 + r2 + 10 >= Width:
            x2 = Width - r2 - 40
        elif x2 - r2 - 10 <= 0:
            x2 = r2 + 40
        speed2[0] = -speed2[0]
        speed2[1] += randint(-3, 3)
    if y2 + r2 + 10 >= Height or y2 - r2 - 10 <= 0:
        if y2 + r2 + 10 >= Height:
            y2 = Height - r2 - 40
        elif y2 - r2 - 10 <= 0:
            y2 = r2 + 40
        speed2[1] = -speed2[1]
        speed2[0] += randint(-3, 3)

    # reflecting from borders with random speed after collision

    f = pygame.font.SysFont('arial', 20)
    screen_text = f.render('Your score: ' + str(counter), 1, RED)
    pos = screen_text.get_rect(topleft=(Width // 14, Height // 10))
    # score bar (another surface)

    screen.fill(BLACK)

    face(x3, y3)

    if i % 20 == 0:
        col1 = COLORS[randint(0, 6)]
        col2 = COLORS[randint(0, 6)]
        i = 0
    # changing color every certain amount of time if it's black ball disappears

    if i % 20 == 0:
        r1 = randint(30, 70)
        r2 = randint(30, 40)
        i = 0
    # changing radius

    new_ball(x1, y1, r1, col1)
    new_ball(x2, y2, r2, col2)

    screen.blit(screen_text, pos)
    # putting score bar on screen

    i += 1

    pygame.display.update()
pygame.quit()

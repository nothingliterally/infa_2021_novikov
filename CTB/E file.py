import pygame
import sys
from random import randint
from pygame.draw import *


pygame.init()
clock = pygame.time.Clock()

Play_Time = 20
# play time in seconds (after that you will die)


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BROWN = (100, 100, 0)
COLORS = [RED, BLUE, WHITE, GREEN, MAGENTA, CYAN,
          BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
          BLACK, BLACK, YELLOW, YELLOW, YELLOW]
k1 = RED
k2 = RED
k3 = RED
k4 = RED

FPS = 60
Height = 750
Width = 1400
screen = pygame.display.set_mode((Width, Height))
# play screen parameters


z = 40
# border thickness


x1 = randint(200, 1100)
y1 = randint(200, 600)
r1 = randint(30, 70)
# 1st circle

x2 = randint(200, 1100)
y2 = randint(200, 600)
r2 = randint(30, 40)
# 2nd circle

x3 = randint(400, 900)
y3 = randint(400, 600)
r3 = randint(120, 180)
# face

x4 = randint(200, 1100)
y4 = randint(200, 600)
r4 = randint(30, 40)
# 3th circle


speed1 = [randint(-4, 4), randint(-4, 4)]
speed2 = [randint(-4, 4), randint(-4, 4)]
speed3 = [randint(-16, 16), randint(-16, 16)]
speed4 = [randint(-6, 6), randint(-6, 6)]
# start speed of objects


counter = 0


# score counter


def face(x, y, r, col):
    """
    This function draws the Yellow Shrek (yes, yellow)
    :param col: BLACK (face disappears) or YELLOW
    :param x: x coordinate of centre
    :param y: y coordinate of centre
    :param r: radius
    """
    if col == BLACK:
        q = 0
    else:
        q = r / 160
    # scaling parameter
    pygame.draw.circle(screen, YELLOW, [x, y], 160 * q)
    # face
    pygame.draw.line(screen, BROWN, [int(-150 * q) + x, int(-150 * q) + y], [int(-30 * q) + x, int(-70 * q) + y],
                     int(15 * q))
    pygame.draw.line(screen, BROWN, [int(30 * q) + x, int(-70 * q) + y], [int(150 * q) + x, int(-150 * q) + y],
                     int(15 * q))
    # eyebrows
    pygame.draw.circle(screen, BLACK, [int(-80 * q) + x, int(-35 * q) + y], int(20 * q) + 1)
    pygame.draw.circle(screen, RED, [int(-80 * q) + x, int(-35 * q) + y], int(45 * q), int(25 * q))
    # 1st eye
    pygame.draw.circle(screen, BLACK, [int(80 * q) + x, int(-35 * q) + y], int(10 * q) + 1)
    pygame.draw.circle(screen, RED, [int(80 * q) + x, int(-35 * q) + y], int(45 * q), int(35 * q))
    # 2nd eye
    pygame.draw.circle(screen, BLACK, [int(40 * q) + x, int(55 * q) + y], int(35 * q), int(10 * q))
    pygame.draw.line(screen, BLACK, [int(20 * q) + x, int(30 * q) + y], [int(-50 * q) + x, int(60 * q) + y],
                     int(10 * q))
    pygame.draw.line(screen, BLACK, [int(60 * q) + x, int(75 * q) + y], [x, int(110 * q) + y], int(10 * q))
    # nose


def new_ball(x, y, r, color):
    """
    This function spawns new circle
    :param x: x coordinate
    :param y: y coordinate
    :param r: radius
    :param color: color
    """
    if color == BLACK:
        circle(screen, color, (x, y), 0)
    else:
        circle(screen, color, (x, y), r)


def click_is_inside(x, y, r, speedx, speedy):
    """
    This function checks your hit and gives you points depending on radius of object
    :param speedy: y speed
    :param speedx: x speed
    :param x: x coordinate of center of a certain object
    :param y: y coordinate of center of a certain object
    :param r: radius of a certain object
    """
    global counter
    if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= (r // 2) ** 2:
        counter += 20 * (speedx ** 2 + speedy ** 2) ** 0.5 / r
    elif (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= r ** 2:
        counter += 10 * (speedx ** 2 + speedy ** 2) ** 0.5 / r


run = Play_Time * 60
i = 0
while run > 0:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_is_inside(x1, y1, r1, speed1[0], speed1[1])
            click_is_inside(x2, y2, r2, speed2[0], speed2[1])
            click_is_inside(x3, y3, r3, speed3[0], speed3[1])
            click_is_inside(x4, y4, r4, speed4[0], speed4[1])

    x1 -= speed1[0]
    y1 -= speed1[1]

    x2 -= speed2[0]
    y2 -= speed2[1]

    x3 += speed3[0]
    y3 += speed3[1]

    x4 += speed4[0]
    y4 += speed4[1]
    # moving our objects

    if x1 + r1 + z >= Width or x1 - r1 - z <= 0:
        if x1 + r1 + z >= Width:
            x1 = Width - r1 - 40
        elif x1 - r1 - z <= 0:
            x1 = r1 + 40
        speed1[0] = -speed1[0]
        speed1[1] += randint(-3, 3)
    if y1 + r1 + z >= Height or y1 - r1 - z <= 0:
        if y1 + r1 + z >= Height:
            y1 = Height - r1 - 40
        elif y1 - r1 - z <= 0:
            y1 = r1 + 40
        speed1[1] = -speed1[1]
        speed1[0] += randint(-3, 3)
    # circle collision with borders and reflection

    if x2 + r2 + z >= Width or x2 - r2 - z <= 0:
        if x2 + r2 + z >= Width:
            x2 = Width - r2 - 40
        elif x2 - r2 - z <= 0:
            x2 = r2 + 40
        speed2[0] = -speed2[0]
        speed2[1] += randint(-3, 3)
    if y2 + r2 + z >= Height or y2 - r2 - z <= 0:
        if y2 + r2 + z >= Height:
            y2 = Height - r2 - 40
        elif y2 - r2 - z <= 0:
            y2 = r2 + 40
        speed2[1] = -speed2[1]
        speed2[0] += randint(-3, 3)
    # circle collision with borders and reflection

    if x3 + r3 + z >= Width or x3 - r3 - z <= 0:
        if x3 + r3 + z >= Width:
            x3 = Width - r3 - 40
        elif x3 - r3 - z <= 0:
            x3 = r3 + 40
        speed3[0] = -speed3[0]
        speed3[1] += randint(-3, 3)
    if y3 + r3 + z >= Height or y3 - r3 - z <= 0:
        if y3 + r3 + z >= Height:
            y3 = Height - r3 - 40
        elif y3 - r3 - z <= 0:
            y3 = r3 + 40
        speed3[1] = -speed3[1]
        speed3[0] += randint(-3, 3)
    # face collision with borders and reflection

    if x4 + r4 + z >= Width or x4 - r4 - z <= 0:
        if x4 + r4 + z >= Width:
            x4 = Width - r4 - 40
        elif x4 - r4 - z <= 0:
            x4 = r4 + 40
        speed4[0] = -speed4[0]
        speed4[1] += randint(-3, 3)
    if y4 + r4 + z >= Height or y4 - r4 - z <= 0:
        if y4 + r4 + z >= Height:
            y4 = Height - r4 - 40
        elif y4 - r4 - z <= 0:
            y4 = r4 + 40
        speed4[1] = -speed4[1]
        speed4[0] += randint(-3, 3)
    # circle collision with borders and reflection

    f1 = pygame.font.SysFont('arial', 20)
    screen_text = f1.render('Your score: ' + str(int(counter * 1000)), True, RED)
    pos1 = screen_text.get_rect(topleft=(Width // 14, Height // 10))
    # score bar (another surface)

    f2 = pygame.font.SysFont('arial', 20)
    screen_text_time = f2.render('Time left: ' + str(int(run // FPS)), True, RED)
    pos2 = screen_text_time.get_rect(topleft=(Width // 14, 30 + Height // 10))
    # time  bar (another surface)

    f3 = pygame.font.SysFont('arial', 20)
    screen_text_hint = f3.render('Pro tip 2: Smaller and/or faster circles you hit -> more points you get', True, GREEN)
    pos3 = screen_text_time.get_rect(topleft=(Width // 14, - 60 + Height // 10))
    # hint  bar (another surface)

    f4 = pygame.font.SysFont('arial', 20)
    screen_text_hint2 = f4.render('Pro tip: Closer to the centre you hit -> more points you get', True, GREEN)
    pos4 = screen_text_time.get_rect(topleft=(Width // 14, - 80 + Height // 10))
    # hint  bar (another surface)

    screen.fill(BLACK)

    if i % randint(20, 30) == 0:
        col1 = COLORS[randint(3, 8)]
        col2 = COLORS[randint(1, 10)]
        col3 = COLORS[randint(6, 16)]
        col4 = COLORS[randint(2, 9)]
        k1 = col1
        k2 = col2
        k3 = col3
        k4 = col4
        i = 0
    # changing color every random amount of time if it's black circle disappears

    if i % randint(20, 40) == 0:
        r1 = randint(10, 70)
        r2 = randint(10, 30)
        r3 = randint(120, 160)
        r4 = randint(30, 40)
        i = 0
    # changing radius every random amount of time (radius is 0 if color is black)

    face(x3, y3, r3, k3)
    new_ball(x1, y1, r1, k1)
    new_ball(x2, y2, r2, k2)
    new_ball(x4, y4, r4, k4)
    # drawing next generation of objects

    pygame.draw.rect(screen, BLUE, (0, 0, Width, z), 0)
    pygame.draw.rect(screen, BLUE, (0, Height - z, Width, Height), 0)
    pygame.draw.rect(screen, BLUE, (0, 0, z, Height), 0)
    pygame.draw.rect(screen, BLUE, (Width - z, 0, Width, Height), 0)
    # borders

    screen.blit(screen_text, pos1)
    screen.blit(screen_text_time, pos2)
    screen.blit(screen_text_hint, pos3)
    screen.blit(screen_text_hint2, pos4)
    # putting bars on screen

    i += 1
    run -= 1

    pygame.display.update()

face(x3, y3, r3, BLACK)
new_ball(x1, y1, r1, BLACK)
new_ball(x2, y2, r2, BLACK)
new_ball(x4, y4, r4, BLACK)
# clearing the screen


pygame.display.update()
pygame.quit()


print("Insert your name:")
Player = input()

fin = open("leaderboard.txt", "at")
fin.write('\n' + Player + " : " + str(int(counter * 1000)))
fin.close()



import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1000, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]
COLORS2 = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK, BLACK, BLACK, BLACK]

global counter
counter = 0
# score counter

global x1, y1, r1, x2, y2, r2, x3, y3, r3


def new_ball():
    """
        creates a new special and regular ball
        x1, y1, r1, x2, y2, r2 are for regular
        x3, y3, r3 are for special
    """
    global x1, y1, r1, x2, y2, r2, x3, y3, r3

    x1 = randint(100, 700)
    y1 = randint(100, 500)
    r1 = randint(30, 50)
    x2 = randint(100, 700)
    y2 = randint(100, 500)
    r2 = randint(30, 50)
    x3 = randint(100, 700)
    y3 = randint(100, 500)
    r3 = randint(10, 30)

    color = COLORS[randint(0, 5)]
    color2 = COLORS2[randint(0, 7)]
    color3 = COLORS2[randint(0, 9)]

    if color2 == BLACK:
        r2 = 0

    if color3 == BLACK:
        r3 = 0

    circle(screen, color, (x1, y1), r1)
    circle(screen, color2, (x2, y2), r2)
    circle(screen, color3, (x3, y3), r3, 1)


def three(x, y, color_hit):
    pygame.draw.line(screen, color_hit, [x - 21, y + 8], [x - 9, y], 4)
    pygame.draw.line(screen, color_hit, [x - 9, y], [x - 21, y], 4)
    pygame.draw.line(screen, color_hit, [x - 21, y], [x - 9, y - 6], 4)
    pygame.draw.line(screen, color_hit, [x - 9, y - 6], [x - 21, y - 6], 4)


def one(x, y, color_hit):
    pygame.draw.line(screen, color_hit, [x - 21, y], [x - 9, y - 6], 4)
    pygame.draw.line(screen, color_hit, [x - 9, y - 6], [x - 9, y + 6], 4)


def zero(x, y, color_hit):
    pygame.draw.line(screen, color_hit, [x - 6, y + 6], [x - 6, y - 6], 4)
    pygame.draw.line(screen, color_hit, [x - 6, y - 6], [x + 6, y - 6], 4)
    pygame.draw.line(screen, color_hit, [x + 6, y - 6], [x + 6, y + 6], 4)
    pygame.draw.line(screen, color_hit, [x + 6, y + 6], [x - 6, y + 6], 4)


def hit_perfect(x, y):
    three(x, y, BLUE)
    zero(x, y, BLUE)
    zero(x + 21, y, BLUE)


def hit_bad(x, y):
    one(x, y, GREEN)
    zero(x, y, GREEN)
    zero(x + 21, y, GREEN)


def hit_perfect_special(x, y):
    pygame.draw.polygon(screen, BLUE, [(x - 12, y + 12), (x - 12, y - 12), (x + 12, y - 12), (x + 12, y + 12)], 0)


def hit_bad_special(x, y):
    pygame.draw.polygon(screen, GREEN, [(x - 12, y + 12), (x - 12, y - 12), (x + 12, y - 12), (x + 12, y + 12)], 0)


def miss(x, y):
    pygame.draw.line(screen, RED, [x - 9, y + 9], [x + 9, y - 9], 4)
    pygame.draw.line(screen, RED, [x - 9, y - 9], [x + 9, y + 9], 4)


def click_is_inside():
    """
        scans your hit and calls score counting function
    """
    if ((event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2) <= (r1 ** 2) / 4:
        score(300)
    elif ((event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2) <= r1 ** 2:
        score(100)
    # 1st regular

    elif ((event.pos[0] - x2) ** 2 + (event.pos[1] - y2) ** 2) <= (r2 ** 2) / 4:
        score(3002)
    elif ((event.pos[0] - x2) ** 2 + (event.pos[1] - y2) ** 2) <= r2 ** 2:
        score(1002)
    # 2nd regular

    elif ((event.pos[0] - x3) ** 2 + (event.pos[1] - y3) ** 2) <= (r3 ** 2) / 4:
        score(6003)
    elif ((event.pos[0] - x3) ** 2 + (event.pos[1] - y3) ** 2) <= r3 ** 2:
        score(2003)
    # special

    else:
        score(0)
    # miss


def score(hit):
    """
    counts your score.
        300 - perfect hit (3002 for second ball)
        100 - bad hit (1002 for second ball)
        0 - miss
        x2 multiplier - for all special targets
        FPS is a multiplier too
    :param hit: type of your hit (perfect, bad or miss)
    """
    global counter

    if hit == 300:

        hit_perfect(x1, y1)

        counter = counter + 300 * FPS
    elif hit == 100:

        hit_bad(x1, y1)

        counter = counter + 100 * FPS
    # 1st regular

    elif hit == 3002:

        hit_perfect(x2, y2)

        counter = counter + 300 * FPS
    elif hit == 1002:

        hit_bad(x2, y2)

        counter = counter + 100 * FPS
    # 2nd regular

    elif hit == 6003:

        hit_perfect_special(x3, y3)

        counter = counter + 600 * FPS
    elif hit == 2003:

        hit_bad_special(x3, y3)

        counter = counter + 200 * FPS
    # special

    elif hit == 0:
        miss(event.pos[0], event.pos[1])
    # miss


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_is_inside()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
    f = pygame.font.SysFont('arial', 20)
    screen_text = f.render("Your score :" + str(counter), 1, RED)
    pos = screen_text.get_rect(topleft=(1000 // 14, 700 // 10))
    screen.blit(screen_text, pos)

high_score = counter
print(high_score)

pygame.quit()

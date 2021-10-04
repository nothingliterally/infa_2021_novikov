import pygame
import math
from pygame.draw import *


def horizons(seasky, seabeach):
    '''
    :param seasky: y coordinate of horizon
    :param seabeach: y coordinate of seashore
    :return: draws background
    '''
    rect(screen, LIGHT_BLUE, (0, 0, 800, 500), 0)  # sky
    rect(screen, YELLOW, (0, seabeach, 800, 500 - seabeach), 0)  # beach
    rect(screen, BLUE, (0, seasky, 800, seabeach - seasky), 0)  # sea


def cloud(xcloud, ycloud, wcloud, hcloud, distance):
    '''
    :param xcloud: x coordinate of upper left corner of rectangle containing bottom left cloud piece
    :param ycloud: y coordinate of upper left corner of rectangle containing bottom left cloud piece
    :param wcloud: width of a single cloud piece
    :param hcloud: height of a single cloud piece
    :param distance: horizontal and vertical distance between upper left corners of rectangles containing cloud pieces
    :return: draws a cloud
    '''
    ellipse(screen, WHITE, (xcloud + 0.5 * distance, ycloud - distance, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + 0.5 * distance, ycloud - distance, wcloud, hcloud), 1)  # 1

    ellipse(screen, WHITE, (xcloud + 1.5 * distance, ycloud - distance, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + 1.5 * distance, ycloud - distance, wcloud, hcloud), 1)  # 2

    ellipse(screen, WHITE, (xcloud, ycloud, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud, ycloud, wcloud, hcloud), 1)  # 3

    ellipse(screen, WHITE, (xcloud + distance, ycloud, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + distance, ycloud, wcloud, hcloud), 1)  # 4

    ellipse(screen, WHITE, (xcloud + 2 * distance, ycloud, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + 2 * distance, ycloud, wcloud, hcloud), 1)  # 5

    ellipse(screen, WHITE, (xcloud + 2.5 * distance, ycloud - distance, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + 2.5 * distance, ycloud - distance, wcloud, hcloud), 1)  # 6

    ellipse(screen, WHITE, (xcloud + 3 * distance, ycloud, wcloud, hcloud))
    ellipse(screen, BLACK, (xcloud + 3 * distance, ycloud, wcloud, hcloud), 1)  # 7


def wavebeach(radius, x0):
    '''
    :param radius: radius of a single wave
    :param x0: quarter-distance between waves
    :return: draws surf
    '''
    for i in range(1, 100, 4):
        y0 = math.sqrt(radius ** 2 - x0 ** 2)
        circle(screen, YELLOW, (i * x0, seabeach + y0), radius)
        circle(screen, BLUE, (i * x0 + 2 * x0, seabeach - y0), radius)


def ship(x0, y0, r, L, d, h, l, a):
    '''
    :param x0: x coordinate of bottom left corner of rectangle containing stern
    :param y0: y coordinate of bottom left corner of rectangle containing stern
    :param r: hull height, stern radius
    :param L: distance between stern and mast
    :param d: mast width
    :param h: mast height
    :param l: distance between mast and bow
    :param a: bow length
    :return: draws a ship
    '''
    line(screen, BLACK, (x0, y0 - r), (x0 + r + L + d + l + a, y0 - r), 3)  # board1

    line(screen, BLACK, (x0, y0 - r), (x0 + r, y0 - r), 4)  # board2

    polygon(screen, BLACK, [(x0 + r + L, y0 - r),
                            (x0 + r + L + d, y0 - r),
                            (x0 + r + L + d, y0 - r - h),
                            (x0 + r + L, y0 - r - h)], 0)  # mast

    arc(screen, BROWN, [x0, y0 - 2 * r + 1, 2 * r, 2 * r], math.pi, 3 * math.pi / 2, 1000000000)
    arc(screen, BLACK, [x0, y0 - 2 * r + 1, 2 * r, 2 * r], math.pi, 3 * math.pi / 2, 1)  # stern

    polygon(screen, BROWN, [(x0 + r + L + d + l, y0),
                            (x0 + r + L + d + l, y0 - r),
                            (x0 + r + L + d + l + a, y0 - r)], 0)  # bow

    polygon(screen, BROWN, [(x0 + r, y0),
                            (x0 + r, y0 - r),
                            (x0 + r + L + d + l, y0 - r),
                            (x0 + r + L + d + l, y0)], 0)  # hull
    polygon(screen, BLACK,
            [(x0 + r + L + d + l, y0),
             (x0 + r + L + d + l, y0 - r),
             (x0 + r + L + d + l + a, y0 - r)], 1)

    polygon(screen, BLACK,
            [(x0 + r, y0),
             (x0 + r, y0 - r),
             (x0 + r + L + d + l, y0 - r),
             (x0 + r + L + d + l, y0)], 1)

    circle(screen, WHITE, (x0 + r + L + d + l + a / 5.1, y0 - r / 2), r / 4.2)
    circle(screen, BLACK, (x0 + r + L + d + l + a / 5.1, y0 - r / 2), r / 4.2, 3)  # window


    polygon(screen, LIGHT_GRAY, [(x0 + r + L + d, y0 - r - h),
                                 (x0 + r + L + d + l / 10, y0 - r - h / 2),
                                 (x0 + r + L + d + l / 2, y0 - r - h / 2)])

    polygon(screen, LIGHT_GRAY, [(x0 + r + L + d, y0 - r),
                                 (x0 + r + L + d + l / 10, y0 - r - h / 2),
                                 (x0 + r + L + d + l / 2, y0 - r - h / 2)])

    polygon(screen, GRAY, [(x0 + r + L + d, y0 - r - h),
                           (x0 + r + L + d + l / 10, y0 - r - h / 2),
                           (x0 + r + L + d + l / 2, y0 - r - h / 2)], 1)

    polygon(screen, GRAY, [(x0 + r + L + d, y0 - r),
                           (x0 + r + L + d + l / 10, y0 - r - h / 2),
                           (x0 + r + L + d + l / 2, y0 - r - h / 2)], 1)
    # sails


def umbrella(x0, y0, q, t, H, D):
    '''
    :param x0: x coordinate of bottom left angle of rectangle containing umbrella
    :param y0: y coordinate of bottom left angle of rectangle containing umbrella
    :param q: half of umbrella head width
    :param t: umbrella head height
    :param H: pole height
    :param D: pole width
    :return: draws an umbrella
    '''
    polygon(screen, BROWN, [(x0 + q, y0),
                            (x0 + q + D, y0),
                            (x0 + q + D, y0 - H),
                            (x0 + q, y0 - H)], 0)

    polygon(screen, BLACK, [(x0 + q, y0),
                            (x0 + q + D, y0),
                            (x0 + q + D, y0 - H),
                            (x0 + q, y0 - H)], 1)

    polygon(screen, LIGHT_BROWN, [(x0, y0 - H),
                                  (x0 + q, y0 - H - t),
                                  (x0 + q + D, y0 - H - t),
                                  (x0 + 2 * q + D, y0 - H)])

    polygon(screen, BLACK, [(x0, y0 - H),
                            (x0 + q, y0 - H - t),
                            (x0 + q + D, y0 - H - t),
                            (x0 + 2 * q + D, y0 - H)], 1)

    line(screen, BLACK, (x0 + q, y0 - H - t), (x0 + q / 3, y0 - H), 1)
    line(screen, BLACK, (x0 + q, y0 - H - t), (x0 + 2 * q / 3, y0 - H), 1)
    line(screen, BLACK, (x0 + q, y0 - H - t), (x0 + q, y0 - H), 1)
    line(screen, BLACK, (x0 + q + D, y0 - H - t), (x0 + q + D, y0 - H), 1)
    line(screen, BLACK, (x0 + q + D, y0 - H - t), (x0 + q + D + q / 3, y0 - H), 1)
    line(screen, BLACK, (x0 + q + D, y0 - H - t), (x0 + q + D + 2 * q / 3, y0 - H), 1)


def sun(x0, y0, R, w, k):
    '''
    :param x0: x coordinate of the center of the sun
    :param y0: y coordinate of the center of the sun
    :param R: radius of the sun
    :param w: ray step
    :param k: ray length
    :return:
    '''
    A = 0.0
    while (A < 2 * math.pi):
        polygon(screen, YELLOW,
                [(x0 + R * math.cos(A) - w * math.sin(A) / 2, y0 + R * math.sin(A) + w * math.cos(A) / 2),
                 (x0 + (R + k) * math.cos(A), y0 + (R + k) * math.sin(A)),
                 (x0 + R * math.cos(A) + w * math.sin(A) / 2, y0 + R * math.sin(A) - w * math.cos(A) / 2),
                 (x0 - R * math.cos(A) + w * math.sin(A) / 2, y0 - R * math.sin(A) - w * math.cos(A) / 2),
                 (x0 - (R + k) * math.cos(A), y0 - (R + k) * math.sin(A)),
                 (x0 - R * math.cos(A) - w * math.sin(A) / 2, y0 - R * math.sin(A) + w * math.cos(A) / 2)], 0)
        A = A + w / R


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
LIGHT_BLUE = (0, 255, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BROWN = (210, 105, 30)
LIGHT_BROWN = (244, 164, 96)
GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)

seabeach = 300
seasky = 200
r = 45
L = 65
d = 4
h = 75
l = 70
a = 60
q = 80
H = 150
t = 60
D = 10
R = 50
w = 6
k = 15

horizons(seasky, seabeach)
cloud(30, 100, 60, 50, 25)
cloud(180, 50, 40, 30, 13)
cloud(420, 90, 70, 80, 35)
wavebeach(40, 20)
ship(500, 250, r, L, d, h, l, a)
ship(200, 220, r / 2, L / 2, d / 2, h / 2, l / 2, a / 2)
umbrella(60, 400, q, t, H, D)
umbrella(250, 400, q / 2, t / 2, H / 2, D / 2)
sun(700, 100, R, w, k)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

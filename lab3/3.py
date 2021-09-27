import pygame
import math
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))

def horizons(seasky, seabeach):
    rect(screen, (0, 255, 255), (0, 0, 10000, 10000), 0)  # sky
    rect(screen, (255, 255, 0), (0, seabeach, 10000, 10000), 0)  # beach
    rect(screen, (0, 0, 255), (0, seasky, 1000, seabeach-seasky), 0)  # sea

def cloud(xcloud, ycloud, wcloud, hcloud, distance):
    ellipse(screen, (255, 255, 255),(xcloud+0.5*distance, ycloud-distance, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+0.5*distance, ycloud-distance, wcloud, hcloud), 1)
    #1

    ellipse(screen, (255, 255, 255), (xcloud+1.5*distance, ycloud-distance, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+1.5*distance, ycloud-distance, wcloud, hcloud), 1)
    #2

    ellipse(screen, (255, 255, 255), (xcloud, ycloud, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud, ycloud, wcloud, hcloud), 1)
    #3

    ellipse(screen, (255, 255, 255), (xcloud+distance, ycloud, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+distance, ycloud, wcloud, hcloud), 1)
    #4

    ellipse(screen, (255, 255, 255), (xcloud+2*distance, ycloud, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+2*distance, ycloud, wcloud, hcloud), 1)
    #5

    ellipse(screen, (255, 255, 255), (xcloud+2.5*distance, ycloud-distance, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+2.5*distance, ycloud-distance, wcloud, hcloud), 1)
    #6

    ellipse(screen, (255, 255, 255), (xcloud+3*distance, ycloud, wcloud, hcloud))
    ellipse(screen, (0, 0, 0), (xcloud+3*distance, ycloud, wcloud, hcloud), 1)
    #7

def wavebeach(radius, x0):
    for i in range(1, 100, 4):
        y0=math.sqrt(radius**2-x0**2)
        circle(screen, (255, 255, 0), (i*x0, seabeach + y0), radius)
        circle(screen, (0, 0, 255), (i*x0+2*x0, seabeach - y0), radius)

def ship(x0, y0, r, L, d, h, l, a):
    line(screen, (0, 0, 0), (x0, y0 - r), (x0+r+L+d+l+a, y0-r), 3)
    #bort

    line(screen, (0, 0, 0), (x0, y0 - r), (x0 + r, y0 - r), 4)
    #bort2

    polygon(screen, (0, 0, 0), [(x0+r+L, y0-r), (x0+r+L+d, y0-r), (x0+r+L+d, y0-r-h), (x0+r+L, y0-r-h)], 0)
    #machta

    arc(screen, (210,105,30), [x0, y0-2*r + 1, 2*r, 2*r], 3.1415926, 3*3.1415926/2, 1000000000)
    arc(screen, (0, 0, 0), [x0, y0 - 2 * r + 1, 2 * r, 2 * r], 3.1415926, 3 * 3.1415926 / 2, 1)
    #brown circle

    polygon(screen, (210,105,30), [(x0+r+L+d+l, y0), (x0+r+L+d+l, y0-r), (x0+r+L+d+l+a, y0-r)], 0)
    polygon(screen, (210,105,30), [(x0+r, y0), (x0+r, y0-r), (x0+r+L+d+l, y0-r), (x0+r+L+d+l, y0)], 0)
    polygon(screen, (0, 0, 0),
            [(x0 + r + L + d + l, y0), (x0 + r + L + d + l, y0 - r), (x0 + r + L + d + l + a, y0 - r)], 1)
    polygon(screen, (0, 0, 0),
            [(x0 + r, y0), (x0 + r, y0 - r), (x0 + r + L + d + l, y0 - r), (x0 + r + L + d + l, y0)], 1)
    #ship

    circle(screen, (255, 255, 255), (x0+r+L+d+l+a/5.1, y0-r/2), r/4.2)
    circle(screen, (0, 0, 0), (x0+r+L+d+l+a/5.1, y0-r/2), r/4.2, 3)
    #window

    polygon(screen, (200,200,200), [(x0+r+L+d, y0-r-h), (x0+r+L+d+l/10, y0-r-h/2), (x0+r+L+d+l/2, y0-r-h/2)])
    polygon(screen, (200,200,200), [(x0+r+L+d, y0-r), (x0+r+L+d+l/10, y0-r-h/2), (x0+r+L+d+l/2, y0-r-h/2)])
    polygon(screen, (50,50,50), [(x0+r+L+d, y0-r-h), (x0+r+L+d+l/10, y0-r-h/2), (x0+r+L+d+l/2, y0-r-h/2)], 1)
    polygon(screen, (50,50,50), [(x0+r+L+d, y0-r), (x0+r+L+d+l/10, y0-r-h/2), (x0+r+L+d+l/2, y0-r-h/2)], 1)
    #parus

def umbrella(x0, y0, q, t, H, D):
    polygon(screen, (210, 105, 30), [(x0 + q, y0),(x0 + q + D, y0),(x0 + q + D, y0 - H),(x0 + q, y0 - H)], 0)
    polygon(screen, (0, 0, 0), [(x0 + q, y0), (x0 + q + D, y0), (x0 + q + D, y0 - H), (x0 + q, y0 - H)], 1)
    polygon(screen, (244, 164, 96), [(x0, y0-H), (x0+q, y0-H-t), (x0+q+D, y0-H-t), (x0+2*q+D, y0-H)])
    polygon(screen, (0, 0, 0), [(x0, y0 - H), (x0 + q, y0 - H - t), (x0 + q + D, y0 - H - t), (x0 + 2 * q + D, y0 - H)], 1)
    line(screen, (0, 0, 0), (x0+q, y0-H-t), (x0+q/3, y0-H), 1)
    line(screen, (0, 0, 0), (x0+q, y0-H-t), (x0+2*q/3, y0-H), 1)
    line(screen, (0, 0, 0), (x0+q, y0-H-t), (x0+q, y0-H), 1)
    line(screen, (0, 0, 0), (x0+q+D, y0-H-t), (x0+q+D, y0-H), 1)
    line(screen, (0, 0, 0), (x0+q+D, y0-H-t), (x0+q+D+q/3, y0-H), 1)
    line(screen, (0, 0, 0), (x0+q+D, y0-H-t), (x0+q+D+2*q/3, y0-H), 1)

def sun(x0, y0, R, w, k):
    A = 0.00000000
    while(A<6.2830):
        polygon(screen, (255, 255, 0), [(x0+R*math.cos(A)-w*math.sin(A)/2, y0+R*math.sin(A) + w*math.cos(A)/2), (x0+(R+k)*math.cos(A), y0+(R+k)*math.sin(A)), (x0+R*math.cos(A)+w*math.sin(A)/2, y0+R*math.sin(A)-w*math.cos(A)/2), (x0-R*math.cos(A)+w*math.sin(A)/2, y0-R*math.sin(A)-w*math.cos(A)/2), (x0-(R+k)*math.cos(A), y0-(R+k)*math.sin(A)), (x0-R*math.cos(A)-w*math.sin(A)/2, y0-R*math.sin(A)+w*math.cos(A)/2)], 0)
        A=A+w/R

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
ship(200, 220, r/2, L/2, d/2, h/2, l/2, a/2)
umbrella(60, 400, q, t, H, D)
umbrella(250, 400, q/2, t/2, H/2, D/2)
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
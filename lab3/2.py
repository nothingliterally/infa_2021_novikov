import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))

rect(screen, (0, 255, 255), (0, 0, 1000,1000), 0)#sky
rect(screen, (255, 255, 0), (0, 350, 1000,200), 0)#beach
rect(screen, (0, 0, 255), (0, 250, 1000,100), 0)#sea

circle(screen, (255, 255, 255), (110, 90), 20)
circle(screen, (0, 0, 0), (110, 90), 20, 1)

circle(screen, (255, 255, 255), (130, 90), 20)
circle(screen, (0, 0, 0), (130, 90), 20, 1)

circle(screen, (255, 255, 255), (100, 100), 20)
circle(screen, (0, 0, 0), (100, 100), 20, 1)

circle(screen, (255, 255, 255), (120, 105), 20)
circle(screen, (0, 0, 0), (120, 105), 20, 1)

circle(screen, (255, 255, 255), (145, 105), 20)
circle(screen, (0, 0, 0), (145, 105), 20, 1)

circle(screen, (255, 255, 255), (155, 90), 20)
circle(screen, (0, 0, 0), (155, 90), 20, 1)

circle(screen, (255, 255, 255), (170, 105), 20)
circle(screen, (0, 0, 0), (170, 105), 20, 1)
#clouds^

circle(screen, (255, 255, 0), (700, 80), 40)
#sun

line(screen, (0,0,0), (550, 180), (550, 280), 7)
#machta

arc(screen, (210,105,30), [400,240, 81, 81], 3.1415926, 3*3.1415926/2, 1000000000)
#brown circle

rect(screen, (210,105,30), (438, 279, 191, 41), 0)
polygon(screen, (210,105,30), [ (629, 279), (629, 319), (709, 279)])
#ship

circle(screen, (255, 255, 255), (645, 295), 10)
circle(screen, (0, 0, 0), (645, 295), 10, 3)
#window

polygon(screen, (200,200,200), [ (554, 180), (570, 230), (640, 230)])
polygon(screen, (200,200,200), [ (554, 280), (570, 230), (640, 230)])
polygon(screen, (50,50,50), [ (554, 180), (570, 230), (640, 230)], 1)
polygon(screen, (50,50,50), [ (554, 280), (570, 230), (640, 230)], 1)
#parus

line(screen, (210,105,30), (110, 300), (110, 450), 7)
polygon(screen, (244,164,96), [ (21, 325), (106, 300), (113, 300), (198, 325)])
line(screen, (210,105,30), (108, 300), (45, 325), 1)
line(screen, (210,105,30), (108, 300), (65, 325), 1)
line(screen, (210,105,30), (108, 300), (85, 325), 1)
line(screen, (210,105,30), (108, 300), (105, 325), 1)
line(screen, (210,105,30), (114, 300), (125, 325), 1)
line(screen, (210,105,30), (114, 300), (145, 325), 1)
line(screen, (210,105,30), (114, 300), (165, 325), 1)
line(screen, (210,105,30), (114, 300), (185, 325), 1)
#umbrella

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

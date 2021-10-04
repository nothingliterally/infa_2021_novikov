import pygame


def drawman(sur: pygame.Surface, x: int, y: int, head: int, scale: float):
    """
this function draws a man
    :param sur: pygame.Surface object
    :param x: x coordinate
    :param y: y coordinate
    :param head: x coordinate parameter
    :param scale: scale
    """
    pygame.draw.ellipse(sur, (185, 155, 191),
                        (x + 220 * head * scale, y + 350 * scale, 150 * head * scale, 300 * scale))
    # body

    pygame.draw.circle(sur, (231, 208, 185), (x + 295 * head * scale, y + 320 * scale), 50 * scale)
    # head

    pygame.draw.lines(sur, (0, 0, 0), False, (
        (x + 335 * head * scale, y + 620 * scale),  # vertical part
        (x + 370 * head * scale, y + 820 * scale),  # vertical part
        (x + 320 * head * scale, y + 820 * scale)), width=2)  # horizontal part
    # first leg

    pygame.draw.lines(sur, (0, 0, 0), False, (
        (x + 255 * head * scale, y + 620 * scale),  # vertical part
        (x + 150 * head * scale, y + 820 * scale),  # vertical part
        (x + 100 * head * scale, y + 820 * scale)), width=2)  # horizontal part
    # second leg

    pygame.draw.line(sur, (0, 0, 0),
                     (x + 250 * head * scale, y + 380 * scale),
                     (x + 150 * head * scale, y + 480 * scale), width=2)
    # first arm

    pygame.draw.line(sur, (0, 0, 0), (x + 340 * head * scale, y + 380 * scale),
                     (x + 470 * head * scale, y + 480 * scale), width=2)
    # second arm


def drawicecream(sur: pygame.Surface, x: int, y: int, head: int, scale: float):
    """
this function draws an ice cream
    :param sur: pygame.Surface object
    :param x: x coordinate
    :param y: y coordinate
    :param head: x coordinate parameter
    :param scale: scale
    """
    pygame.draw.polygon(sur, (227, 201, 67), (
        (x + 160 * head * scale, y + 480 * scale),
        (x + 110 * head * scale, y + 460 * scale),
        (x + 165 * head * scale, y + 420 * scale)))
    # рожок

    pygame.draw.circle(sur, (255, 0, 0), (x + 145 * head * scale, y + 425 * scale), 18 * scale)
    # шарик от мороженого 1
    pygame.draw.circle(sur, (95, 0, 0), (x + 120 * head * scale, y + 445 * scale), 18 * scale)
    # шарик от мороженого 2
    pygame.draw.circle(sur, (255, 255, 255), (x + 120 * head * scale, y + 420 * scale), 18 * scale)
    # шарик от мороженого 3


def drawwoman(sur: pygame.Surface, x: int, y: int, head: int, scale: float):
    """
this function draws a woman
    :param sur: pygame.Surface object
    :param x: x coordinate
    :param y: y coordinate
    :param head: x coordinate parameter
    :param scale: scale
    """
    pygame.draw.polygon(sur, (255, 95, 177), (
        (x + 620 * head * scale, y + 350 * scale),
        (x + 540 * head * scale, y + 650 * scale),
        (x + 700 * head * scale, y + 650 * scale)))
    # body

    pygame.draw.circle(sur, (231, 208, 185), (x + 620 * head * scale, y + 320 * scale), 50 * scale)
    # head

    pygame.draw.lines(sur, (0, 0, 0), False, (
        (x + 600 * head * scale, y + 650 * scale),  # vertical part
        (x + 600 * head * scale, y + 820 * scale),  # vertical part
        (x + 550 * head * scale, y + 825 * scale)), width=2)  # horizontal part
    # first leg

    pygame.draw.lines(sur, (0, 0, 0), False, (
        (x + 640 * head * scale, y + 650 * scale),  # vertical part
        (x + 640 * head * scale, y + 820 * scale),  # vertical part
        (x + 690 * head * scale, y + 820 * scale)), width=2)  # horizontal part
    # second leg

    pygame.draw.line(sur, (0, 0, 0),
                     (x + 605 * head * scale, y + 410 * scale),
                     (x + 470 * head * scale, y + 480 * scale), width=2)
    # arm connected with men

    pygame.draw.lines(sur, (0, 0, 0), False, (
        (x + 635 * head * scale, y + 410 * scale),
        (x + 680 * head * scale, y + 455 * scale),
        (x + 740 * head * scale, y + 440 * scale)), width=2)
    # arm connected with common ice cream


def drawballoon(sur: pygame.Surface, x: int, y: int, head: int, scale: float):
    """
this function draws a balloon
    :param sur: pygame.Surface object
    :param x: x coordinate
    :param y: y coordinate
    :param head: x coordinate parameter
    :param scale: scale
    """
    pygame.draw.polygon(sur, (255, 0, 0), (
        (x + 800 * head * scale, y + 300 * scale),
        (x + 850 * head * scale, y + 250 * scale),
        (x + 790 * head * scale, y + 230 * scale)))
    # triangle part of balloon

    pygame.draw.circle(sur, (255, 0, 0), (x + 835 * head * scale, y + 240 * scale), 18 * scale)
    # top of balloon
    pygame.draw.circle(sur, (255, 0, 0), (x + 807 * head * scale, y + 230 * scale), 18 * scale)
    # top of balloon


pygame.init()
screen = pygame.display.set_mode((1500, 1000))  # screen size
clock = pygame.time.Clock()
cream = pygame.Surface((500, 500))  # ice cream surface

pygame.draw.rect(screen, (143, 198, 246), (0, 0, 1500, 500))  # sky
pygame.draw.rect(screen, (103, 217, 108), (0, 500, 1500, 500))  # ground

drawman(screen, 120, 180, 1, 0.85)
drawwoman(screen, 120, 180, 1, 0.85)
# left pair of people

drawwoman(screen, 1380, 180, -1, 0.85)
drawman(screen, 1380, 180, -1, 0.85)
# right pair of people

drawballoon(screen, 1400, 0, -1, 1.5)
# balloon
pygame.draw.line(screen, (0, 0, 0), (250, 600), (200, 450), width=2)
# balloon's stick

drawicecream(screen, 1490, -120, -1, 1.5)
# man's ice cream
drawicecream(cream, 0, -700, 1, 2)
# women's ice cream (the middle one)

pygame.draw.line(screen, (0, 0, 0), (770, 260), (750, 560), width=2)
# middle ice cream stick

cream = pygame.transform.rotate(cream, -25)
cream.set_colorkey((0, 0, 0))
screen.blit(cream, (380, -100))
# middle ice cream rotate

pygame.display.update()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

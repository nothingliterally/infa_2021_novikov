import math
from random import randint
from random import choice

import pygame

FPS = 30
Play_Time = 20
# play time in seconds (after that you will die)

RED = 0xFF0000
BLUE = 0x0000FF
DARK_BLUE = 0x000099
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [GREY, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, g):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = g.x
        self.y = g.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 150  # переменная определяющая время жизни снаряда
        self.index = 1  # индикатор типа снаряда

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x >= 800 - self.r * self.index:
            self.vx = -self.vx
            self.x = 800 - self.r * self.index - 1
        if self.y >= 600 - self.r * self.index:
            self.vy = -(self.vy * 0.7) // 1
            self.vx = (self.vx * 0.7) // 1
            self.y = 600 - self.r * self.index - 1
        if abs(self.vy // 1) == 0 and self.y - (600 - 5) >= -1:
            self.vx = 0
        self.vy = self.vy - 1
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        """
        Рисует шар, которым мы стреляем
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r * self.index
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r * self.index) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = randint(40, 600)
        self.y = 450
        self.r = 10
        self.sign = 1  # переменная опрделеющая справа или слева от пушки находится курсор

    def fire2_start(self, event):
        if event:
            self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self)
        new_ball.r += 5

        if self.f2_power >= 100:
            new_ball.index = 3
            new_ball.live = 9999999 * 5

        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) / new_ball.index
        new_ball.vy = - self.f2_power * math.sin(self.an) / new_ball.index
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] == self.x:
                self.an = 999999999
                self.sign = 1
            else:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
        if event.pos[0] - self.x > 0:
            self.sign = 1
        elif event.pos[0] - self.x < 0:
            self.sign = -1

    def draw(self):
        """
        Рисует пушку
        """
        pygame.draw.polygon(
            self.screen,
            self.color,
            [
                [self.x - 3 * math.sin(self.an), self.y + 3 * math.cos(self.an)],
                [self.x + 3 * math.sin(self.an), self.y - 3 * math.cos(self.an)],
                [self.x + self.sign * self.f2_power * math.cos(self.an) + 3 * math.sin(self.an),
                 self.y + self.sign * self.f2_power * math.sin(self.an) - 3 * math.cos(self.an)],
                [self.x + self.sign * self.f2_power * math.cos(self.an) - 3 * math.sin(self.an),
                 self.y + self.sign * self.f2_power * math.sin(self.an) + 3 * math.cos(self.an)]
            ], 0)

    def move(self, event):
        """
        moves 1st cannon
        """
        if event.key == pygame.K_RIGHT:
            self.x += 10
        elif event.key == pygame.K_LEFT:
            self.x -= 10

    def power_up(self):
        """
        показатель начальной скорости снаряда
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move2(self, event):
        """
        moves 2nd cannon
        """
        if event.key == pygame.K_d:
            self.x += 10
        elif event.key == pygame.K_a:
            self.x -= 10


class Target:
    def new_target(self):
        """
        Задаёт новую мишень
        """
        self.live = 1
        self.color = DARK_BLUE
        self.r = randint(2, 50)
        self.y = randint(300, 550)
        self.x = randint(600, 780)
        target.draw()

    def another_new_target(self):
        """
        Задаёт новую мишень другого типа
        """
        self.live = 1
        self.color = BLACK
        self.r = randint(2, 50)
        self.y = randint(300, 550)
        self.x = randint(600, 780)
        target.another_draw()

    def __init__(self):
        self.points = 0
        self.live = 1
        self.color = DARK_BLUE
        self.r = randint(2, 50)
        self.y = randint(300, 550)
        self.x = randint(600, 780)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """
        Рисует мишень
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def bomb_draw(self):
        """
        Рисует мишень
        """
        pygame.draw.circle(screen, RED, (self.x, self.y), self.r)

    def another_draw(self):
        """
        Рисует мишень другого типа
        """
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.r)

    def target_move(self):
        """
        Задаёт движение мишени
        """
        if self.x > 800 - self.r:
            self.vx = -self.vx
            self.x -= self.r
        if self.x < self.r:
            self.vx = -self.vx
            self.x = self.r
        if self.y > 600 - self.r:
            self.vy = -self.vy
            self.vx = self.vx
            self.y -= (self.y - 600 + self.r)
        if self.y < self.r:
            self.vy = -self.vy
            self.y = self.r
        self.x += self.vx
        self.y -= self.vy

    def another_target_move(self):
        """
        Перемещение мишени другого типа
        """
        if self.x > 800 - self.r:
            self.vx = -self.vx
            self.x = 800 - self.r
        if self.y > 600 - self.r:
            self.vy = -self.vy
            self.vx = self.vx
            self.y = 600 - self.r
        if self.x < self.r:
            self.vx = -self.vx
            self.x = self.r
        self.vy = self.vy - 1
        self.x += self.vx
        self.y -= self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
gun2 = Gun(screen)
target = Target()
target2 = Target()
target3 = Target()
bomb1 = Target()
bomb2 = Target()
finished = False

run = Play_Time * FPS

while run > 0:
    screen.fill(WHITE)
    gun.draw()
    gun2.draw()
    target.draw()
    target2.draw()
    target3.another_draw()
    bomb1.bomb_draw()
    bomb2.bomb_draw()

    bomb1.target_move()
    bomb2.target_move()
    target.target_move()
    target2.target_move()
    target3.another_target_move()

    f1 = pygame.font.SysFont('arial', 20)
    screen_text = f1.render('Your score: ' + str(target.points + target2.points + target3.points), True, BLACK)
    pos1 = screen_text.get_rect(topleft=(WIDTH // 14, HEIGHT // 11))
    # окошко подсчёта очков

    f2 = pygame.font.SysFont('arial', 20)
    screen_text_time = f2.render('Time left: ' + str(int(run // FPS)), True, RED)
    pos2 = screen_text_time.get_rect(topleft=(WIDTH // 14, 30 + HEIGHT // 10))
    # time  bar (another surface)

    f3 = pygame.font.SysFont('arial', 20)
    screen_text_hint = f3.render(
        'Pro tip: Hold until power reaches max length and shoot to get big and almost invincible ball', True, BLACK)
    pos3 = screen_text.get_rect(topleft=(WIDTH // 14, 30 + HEIGHT // 6))
    f4 = pygame.font.SysFont('arial', 15)
    screen_text_hint_2 = f4.render('You can move your cannon by using LEFT//RIGHT & A//D keys and shoot using MOUSE1 and MOUSE2. RED BOMBS KILL YOU',
                                   True, BLACK)
    pos4 = screen_text.get_rect(topleft=(WIDTH // 14, 30 + HEIGHT // 4))
    # окошко подсказок

    screen.blit(screen_text, pos1)
    screen.blit(screen_text_time, pos2)
    screen.blit(screen_text_hint, pos3)
    screen.blit(screen_text_hint_2, pos4)
    # "рисование" окошка подсчетов и времени на экране

    for b in balls:
        if b.live > 0:
            b.draw()

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        elif event.type == pygame.KEYDOWN:
            gun.move(event)
            gun2.move2(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gun.fire2_start(event)
            elif event.button == 3:
                gun2.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                gun.fire2_end(event)
            elif event.button == 3:
                gun2.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun2.targetting(event)

    if (gun.x - bomb1.x) ** 2 + (gun.y - bomb1.y) ** 2 <= bomb1.r ** 2:
        run = 0
    if (gun.x - bomb2.x) ** 2 + (gun.y - bomb2.y) ** 2 <= bomb2.r ** 2:
        run = 0
    if (gun2.x - bomb1.x) ** 2 + (gun2.y - bomb1.y) ** 2 <= bomb1.r ** 2:
        run = 0
    if (gun2.x - bomb2.x) ** 2 + (gun2.y - bomb2.y) ** 2 <= bomb2.r ** 2:
        run = 0
    # условие смерти от бомб

    for b in balls:
        b.move()
        b.live -= 1

        if b.hittest(target) and target.live and b.live > 0:
            target.live = 0
            b.live -= 9999999
            target.hit()
            target.new_target()
        elif b.hittest(target2) and target2.live and b.live > 0:
            target2.live = 0
            b.live -= 9999999
            target2.hit()
            target2.new_target()
        elif b.hittest(target3) and target3.live and b.live > 0:
            target3.live = 0
            b.live -= 9999999
            target3.hit()
            target3.another_new_target()

    gun.power_up()
    gun2.power_up()

    run -= 1

pygame.quit()

print("Insert your name:")
Player = input()

fin = open("leaderboard_gun.txt", "at")
fin.write('\n' + Player + " : " + str(int(target.points + target2.points + target3.points)))
fin.close()

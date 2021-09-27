import math
import turtle as t
from random import *
number_of_turtles = 5

def vector(unit, move):
    unit.goto(unit.xcor() + move[0], unit.ycor() + move[1])

width = 150
height = 250

t.up()
t.goto(-width, height)
t.down()
t.goto(width, height)
t.goto(width, -height)
t.goto(-width, -height)
t.goto(-width, height)

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.pu()
    unit.speed(0)
    unit.goto(randint(-width, width), randint(-height, height))
    # unit.pd()

speeds = []
for i in range(number_of_turtles):
    speeds.append([randint(-5, 5), randint(-5, 5)])

while True:
    for i in range(number_of_turtles):
        vector(pool[i], speeds[i])
        if abs(pool[i].xcor()) >= width:
            speeds[i][0] = -speeds[i][0]
        if abs(pool[i].ycor()) >= height:
            speeds[i][1] = -speeds[i][1]
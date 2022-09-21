import imp
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)


turtles = []
x_positions = [0, -20, -40]
for x_pos in x_positions:
    new_turtle = Turtle(shape='square')
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.goto(x=x_pos, y=0)
    turtles.append(new_turtle)

while True:
    screen.update()
    time.sleep(0.1)
    for turtle in range(len(turtles) - 1, 0, -1):
        new_pos = (turtles[turtle - 1].position())
        turtles[turtle].goto(new_pos)
    turtles[0].forward(20)
    turtles[0].left(90)
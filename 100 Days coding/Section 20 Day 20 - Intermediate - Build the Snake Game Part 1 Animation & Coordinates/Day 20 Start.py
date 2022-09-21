from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')
x_positions = [-40, -20, 0]
turtles = []
for x_pos in x_positions:
    turtle = Turtle(shape = 'square')
    turtle.color('white')
    turtle.penup()
    turtle.goto(x = x_pos, y = 0)
    turtles.append(turtle)

screen.exitonclick()
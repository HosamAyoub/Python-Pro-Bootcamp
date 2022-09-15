from turtle import Turtle, Screen
from random import randint
import turtle

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb

tom = Turtle()
turtle.colormode(255)
tom.speed(0)
for angle in range(0, 360, 5):
    tom.color(random_color())
    tom.setheading(angle)
    tom.circle(100)

screen_time = Screen()
screen_time.exitonclick()
from turtle import Turtle, Screen
from random import choice, randint
import turtle

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb

tom = Turtle()
# colors = ["black", "gray", "light gray", "blue", "midnight blue", "cyan", "green", "dark green", "light green", "red", "orange", "purple", "brown"]
turtle.colormode(255)
tom.speed(5)
tom.pensize(10)
for _ in range(100):
    tom.color(random_color())
    tom.setheading(90*randint(0, 3))
    tom.forward(100)

screen_time = Screen()
screen_time.exitonclick()
from turtle import Turtle, Screen
from random import choice

tom = Turtle()
colors = ["black", "gray", "light gray", "alice blue", "blue", "midnight blue", "cyan", "green", "dark green", "light green", "red", "orange", "purple", "brown"]
for sides in range(3, 11):
    tom.color(choice(colors))
    for side in range(sides):
        tom.right(360/sides)
        tom.forward(100)

screen_time = Screen()
screen_time.exitonclick()
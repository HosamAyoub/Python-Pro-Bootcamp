from turtle import Turtle, Screen
from random import choice, randint

tom = Turtle()
colors = ["black", "gray", "alice blue", "blue", "midnight blue", "cyan", "green", "dark green", "light green", "red", "orange", "purple", "brown"]
tom.speed(6)
tom.pensize(8)
for sides in range(100):
    tom.color(choice(colors))
    tom.right(90*randint(0, 3))
    tom.forward(100)

screen_time = Screen()
screen_time.exitonclick()